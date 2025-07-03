import yaml
import webbrowser
import json
import threading
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import secrets
import hashlib
import base64

# --- 常量配置 ---
TOKEN_FILE = 'schwabs_token.json'
CONFIG_FILE = 'config.yaml'

# 全局变量用于在线程间传递授权码
authorization_code = None
auth_error = None

def load_config():
    """从YAML文件加载配置"""
    try:
        # 注意: 你的config.yaml在config/目录下，所以路径需要调整
        # 如果你的config.yaml在根目录，就用 'config.yaml'
        # 修改后
        with open('config/config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"错误: 配置文件 'config/config.yaml' 未找到。请检查路径。")
        exit(1)

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """一个简单的HTTP请求处理器，用于捕获OAuth回调"""
    def do_GET(self):
        print(f"--> [RAW REQUEST] Path: {self.path}")
        global authorization_code, auth_error
        parsed_path = urlparse(self.path)
        query_components = parse_qs(parsed_path.query)

        # The callback will come to the root path '/', so we check for 'code' or 'error' first.
        if 'code' in query_components:
            authorization_code = query_components["code"][0]
            print(f"\n[OAuthCallbackHandler] 获取到授权码: {authorization_code}")
            message = b"<h1>Authentication Successful!</h1><p>You can close this browser window now.</p>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(message)
        elif 'error' in query_components:
            auth_error_msg = query_components.get("error", ["Unknown error"])[0]
            error_desc = query_components.get('error_description', ['No description.'])[0]
            auth_error = f"{auth_error_msg}: {error_desc}"
            print(f"[OAuthCallbackHandler] 授权失败: {auth_error}")
            message = f"<h1>Authentication Failed!</h1><p>Error: {auth_error}. Please check the console.</p>".encode('utf-8')
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(message)
        elif parsed_path.path == '/favicon.ico':
            self.send_response(204)  # No Content
            self.end_headers()
        else:
            # This is for the direct access test or other unknown requests
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Service Ready. Waiting for callback.')

    def log_message(self, format, *args):
        # Print full request URL and headers for debugging
        print(f"[HTTP] {self.address_string()} - {self.path} - Headers: {self.headers}")
        # Or, for more detail, use the following, but be cautious about printing sensitive information:
        # print(f"[HTTP] {self.requestline} - Headers: {dict(self.headers)}")

def run_callback_server(host, port, timeout):
    """运行一个临时的本地HTTP服务器来监听回调（不再使用SSL）"""
    import time
    import traceback
    global authorization_code, auth_error
    try:
        server_address = (host, port)
        with HTTPServer(server_address, OAuthCallbackHandler) as httpd:
            print(f"[run_callback_server] 已启动本地HTTP监听: http://{host}:{port}")
            start_time = time.time()
            while authorization_code is None and auth_error is None:
                httpd.timeout = 1  # Check every second
                httpd.handle_request()
                if time.time() - start_time > timeout:
                    # This message is a fallback, the main timeout is in get_new_token
                    break
    except Exception as e:
        print(f"本地HTTP服务器启动失败: {e}")
        auth_error = str(e)
        print(traceback.format_exc())

def generate_pkce_pair():
    code_verifier = secrets.token_urlsafe(64)[:128]
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode('ascii')).digest()
    ).rstrip(b'=') .decode('ascii')
    return code_verifier, code_challenge

def get_new_token():
    """执行完整的OAuth 2.0流程以获取新令牌"""
    config = load_config()
    api_key = config['api_key']
    api_secret = config['api_secret']
    callback_url = config['callback_url']
    
    # Load new settings from config, with defaults
    callback_host = config.get('local_server_host', '127.0.0.1')
    callback_port = config.get('local_server_port', 5000)
    auth_timeout = config.get('auth_timeout', 120)

    print(f"\n[get_new_token] Loaded configuration: {config}")  # Print full config

    if 'localhost' in callback_url or '127.0.0.1' in callback_url:
        print("="*80)
        print("⚠️ 警告: 回调URL看起来是一个本地地址(localhost)。")
        print("Schwab API需要一个公开的HTTPS地址进行回调，例如由ngrok提供。")
        print("="*80)

    print(f"使用的回调URL: {callback_url}")
    print(f"本地监听地址: http://{callback_host}:{callback_port}")
    print(f"授权超时设置为: {auth_timeout} 秒")
    print(f"\n请确保:\n 1. ngrok已启动并指向本地端口 (命令: ngrok http {callback_port})\n 2. Schwab开发者门户中的'Callback URL'已精确设置为ngrok提供的HTTPS地址。\n 3. config.yaml中的'callback_url'也已设置为该ngrok地址。")

    auth_url = 'https://api.schwabapi.com/v1/oauth/authorize'
    token_url = 'https://api.schwabapi.com/v1/oauth/token'

    try:
        code_verifier, code_challenge = generate_pkce_pair()
        schwab = OAuth2Session(
            client_id=api_key,
            redirect_uri=callback_url,
            scope=['accounts', 'trading', 'marketdata', 'offline_access']
        )
        authorization_url, state = schwab.authorization_url(
            auth_url,
            code_challenge=code_challenge,
            code_challenge_method='S256'
        )

        print("\n" + "="*80)
        print("程序即将自动打开浏览器进行Schwab授权。请按提示操作。")
        print(f"--> 生成的授权URL: {authorization_url}")
        print(f"--> 生成的 State: {state}")
        print("="*80)
        webbrowser.open(authorization_url)

        server_thread = threading.Thread(target=run_callback_server, args=(callback_host, callback_port, auth_timeout))
        server_thread.daemon = True # Allows main thread to exit even if this thread is running
        server_thread.start()
        
        # Wait for the thread to finish (i.e., code is received) or for the timeout
        server_thread.join(timeout=auth_timeout)

        if server_thread.is_alive():
            print(f"\n操作超时（超过 {auth_timeout} 秒）。用户可能未完成授权。")
            return None

        if auth_error:
            print(f"\n授权失败: {auth_error}")
            return None
        if not authorization_code:
            print("\n错误: 未能从Schwab回调中获取授权码。请检查回调URL配置。")
            return None

        print("\n✅ 授权码获取成功! 正在换取访问令牌(Access Token)...")

        auth = HTTPBasicAuth(api_key, api_secret)
        token = schwab.fetch_token(
            token_url=token_url,
            code=authorization_code,
            auth=auth,
            code_verifier=code_verifier
        )

        with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
            json.dump(token, f, indent=4)
        print(f"\n✅ 巨大成功! 令牌已保存到 '{TOKEN_FILE}' 文件中。")
        return token
    except Exception as e:
        print(f"\n❌ 交换令牌时发生错误: {str(e)}")
        print("详细错误信息:")
        import traceback
        print(traceback.format_exc())
        return None
    
if __name__ == '__main__':
    get_new_token()