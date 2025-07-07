import yaml
import webbrowser
import json
import threading
import ssl
import os
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

import secrets
import hashlib
import base64
from OpenSSL import crypto # Moved to top-level for IDE compatibility and clearer dependency

# --- 常量配置 ---
TOKEN_FILE = 'schwabs_token.json'
CONFIG_FILE = 'config.yaml'
CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

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
            config = yaml.safe_load(f)
            # 默认不使用ngrok
            config['use_ngrok'] = config.get('use_ngrok', False)
            return config
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

def generate_self_signed_cert(cert_file, key_file):
    """生成自签名SSL证书和私钥"""
    if os.path.exists(cert_file) and os.path.exists(key_file):
        print(f"证书文件 '{cert_file}' 和 '{key_file}' 已存在，跳过生成。")
        return

    print(f"正在生成自签名SSL证书 '{cert_file}' 和私钥 '{key_file}'...")
    try:
        from OpenSSL import crypto

        # 创建一个自签名证书
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)

        cert = crypto.X509()
        cert.get_subject().C = "US"
        cert.get_subject().ST = "State"
        cert.get_subject().L = "City"
        cert.get_subject().O = "SchwabGridTrader"
        cert.get_subject().OU = "Development"
        cert.get_subject().CN = "localhost" # Common Name must be localhost for 127.0.0.1
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365 * 24 * 60 * 60) # Valid for 1 year
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        with open(cert_file, "wt") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
        with open(key_file, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
        print("证书生成成功。")
    except ImportError:
        print("错误: 未安装 'pyOpenSSL' 库。请运行 'pip install pyOpenSSL' 来生成自签名证书。")
        print("或者手动生成证书并将其命名为 'cert.pem' 和 'key.pem' 放在项目根目录。")
        exit(1)
    except Exception as e:
        print(f"生成证书时发生错误: {e}")
        exit(1)

def run_callback_server(host, port, timeout):
    """运行一个临时的本地HTTPS服务器来监听回调"""
    import time
    import traceback
    global authorization_code, auth_error
    try:
        server_address = (host, port)
        httpd = HTTPServer(server_address, OAuthCallbackHandler)
        
        # 配置SSL/TLS
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
            print(f"[run_callback_server] 已启动本地HTTPS监听: https://{host}:{port}")
        except FileNotFoundError:
            print(f"错误: 证书文件 '{CERT_FILE}' 或 '{KEY_FILE}' 未找到。请确保它们在项目根目录。")
            print("尝试运行脚本以自动生成证书，或手动生成。")
            auth_error = "SSL证书文件缺失"
            return
        except ssl.SSLError as e:
            print(f"SSL配置错误: {e}")
            print("请检查证书文件是否有效。")
            auth_error = "SSL配置错误"
            return

        start_time = time.time()
        while authorization_code is None and auth_error is None:
            httpd.timeout = 1  # Check every second
            httpd.handle_request()
            if time.time() - start_time > timeout:
                break
    except Exception as e:
        print(f"本地HTTPS服务器启动失败: {e}")
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
    use_ngrok = config['use_ngrok']
    
    # Load new settings from config, with defaults
    callback_host = config.get('local_server_host', '127.0.0.1')
    callback_port = config.get('local_server_port', 5000)
    auth_timeout = config.get('auth_timeout', 120)

    print(f"\n[get_new_token] Loaded configuration: {config}")  # Print full config

    if not use_ngrok:
        # 确保证书存在
        generate_self_signed_cert(CERT_FILE, KEY_FILE)
        print(f"使用的回调URL: {callback_url}")
        print(f"本地监听地址: https://{callback_host}:{callback_port}")
        print(f"授权超时设置为: {auth_timeout} 秒")
        print(f"\n请确保:\n 1. Schwab开发者门户中的'Callback URL'已精确设置为: {callback_url}\n 2. config.yaml中的'callback_url'也已设置为该地址。")
        print("由于使用自签名证书，浏览器可能会提示不安全，请选择继续访问。")
    else:
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
            scope=['api']
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
        # 最小化scope，仅用一个scope做测试
        token = None
        try:
            token = schwab.fetch_token(
                token_url=token_url,
                code=authorization_code,
                auth=auth,
                code_verifier=code_verifier,
                scope=['api']
            )
        except Exception as e:
            print("\n❌ fetch_token发生错误: ", str(e))
            # 尽可能打印所有能拿到的原始响应内容
            response = getattr(e, 'response', None)
            if response is not None:
                print('Token endpoint raw response:', response.text)
            elif hasattr(e, 'description'):
                print('OAuthlib error description:', getattr(e, 'description'))
            else:
                print('Exception object:', repr(e))
            import traceback
            print(traceback.format_exc())
            raise

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