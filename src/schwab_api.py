import json
import yaml  # 移除了 time，因为它没有被使用
from requests_oauthlib import OAuth2Session

# --- 路径配置 ---
TOKEN_FILE = 'schwabs_token.json'
# 【已修正】指向 config 子目录下的配置文件
CONFIG_FILE = 'config/config.yaml' 

class SchwabAPI:
    def __init__(self):
        self.config = self._load_config()
        self.token = self._load_token()
        self.client_id = self.config['api_key']
        self.client_secret = self.config['api_secret']
        self.token_url = 'https://api.schwabapi.com/v1/oauth/token'

        # 创建一个可自动刷新token的会话
        self.session = OAuth2Session(
            client_id=self.client_id,
            token=self.token,
            auto_refresh_url=self.token_url,
            auto_refresh_kwargs={'client_id': self.client_id, 'client_secret': self.client_secret},
            token_updater=self._save_token
        )

    def _load_config(self):
        """加载YAML配置文件"""
        try:
            # 【已确认】使用正确的编码读取
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            # 提供了更清晰的错误指引
            raise Exception(f"配置文件 ({CONFIG_FILE}) 未找到。请确保该文件存在并且路径正确。")

    def _load_token(self):
        """加载JSON格式的token文件"""
        try:
            # 【已优化】为读取json文件也加上编码，保持代码风格统一
            with open(TOKEN_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Token文件 ({TOKEN_FILE}) 未找到。请先成功运行 auth_manager.py。")

    def _save_token(self, token):
        """保存更新后的token到文件"""
        self.token = token
        # 【已优化】为写入json文件也加上编码和美化输出
        with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
            json.dump(token, f, indent=4)
        print("Token已刷新并保存。")

    def get_account_numbers(self):
        """获取所有关联账户的哈希值ID"""
        url = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"
        response = self.session.get(url)
        response.raise_for_status()  # 如果请求失败(如4xx, 5xx错误)则抛出异常
        return response.json()

    def get_account_info(self, account_hash, fields='positions'):
        """
        获取单个账户的详细信息。
        :param account_hash: 账户的哈希值
        :param fields: 'positions', 'orders' 等，可以是逗号分隔的字符串
        """
        url = f"https://api.schwabapi.com/trader/v1/accounts/{account_hash}"
        params = {'fields': fields}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

# --- 用于直接运行此文件进行测试 ---
if __name__ == '__main__':
    try:
        api = SchwabAPI()
        print("✅ API客户端初始化成功！")
        
        # 1. 获取账户哈希
        print("\n⏳ 正在获取账户列表...")
        accounts = api.get_account_numbers()
        
        if not accounts:
            print("❌ 未能找到任何账户。请检查您的Schwab账户是否已正确关联。")
        else:
            print(f"✅ 成功找到 {len(accounts)} 个账户。")
            
            # 2. 获取第一个账户的详细信息
            first_account_hash = accounts[0]['hashValue']
            print(f"\n⏳ 正在获取账户 {first_account_hash} 的详细信息(含持仓)...")
            account_details = api.get_account_info(first_account_hash)
            
            print("\n--- 账户详情 ---")
            # 使用json.dumps美化打印输出
            print(json.dumps(account_details, indent=2))
            print("✅ 测试完成！")
            
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")