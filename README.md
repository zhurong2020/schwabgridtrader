# SchwabGridTrader

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-green.svg)

An API integration module for Charles Schwab platform, providing robust OAuth 2.0 authentication, token management, and basic API client functionalities. This module is designed to be integrated into larger trading applications, such as a grid trading tool, to enable secure and reliable interaction with Schwab's APIs.

一个用于嘉信理财 (Charles Schwab) 平台的API集成模块，提供强大的OAuth 2.0认证、令牌管理和基本的API客户端功能。该模块旨在集成到更大的交易应用程序（例如网格交易工具）中，以实现与Schwab API的安全可靠交互。

## 主要功能 (Key Features)

- **OAuth 2.0 认证与令牌管理:**
    - 实现与嘉信理财 API 的安全 OAuth 2.0 授权码流程，支持 PKCE。
    - 支持在本地开发环境（如 WSL）中启动 **本地 HTTPS 回调服务器**，简化调试。
    - 自动获取、存储和刷新 Access Token 和 Refresh Token，确保会话持久性。
    - 敏感令牌文件 `schwabs_token.json` 已自动添加到 `.gitignore`。
- **Schwab API 客户端:**
    - 提供与嘉信理财 API 的安全、可靠连接。
    - 能够获取账户授权和基本账户信息（如持仓）。
    - 模块化设计，易于集成到其他 Python 项目中。

## 开始使用 (Getting Started)

### 1. 前提条件 (Prerequisites)

- Python 3.8 或更高版本
- 一个已激活API交易权限的 Charles Schwab 账户
- 在 [Schwab Developer Portal](https://developer.schwab.com/) 创建的应用，并获取 `App Key` 和 `App Secret`。

### 2. 安装 (Installation)

1.  **克隆仓库:**
    ```bash
    git clone https://github.com/your-username/SchwabGridTrader.git
    cd SchwabGridTrader
    ```

2.  **安装依赖:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. 配置 API 凭据和回调 URL (Configure API Credentials and Callback URL)

- 编辑 `config/config.yaml` 文件，填入你的 `api_key` 和 `api_secret`。
- 在 Schwab 开发者门户和 `config/config.yaml` 中设置相同的回调 URL (`callback_url`)。**注意：** 对于本地开发，强烈建议使用 `https://127.0.0.1:PORT` 作为回调 URL，并确保 `use_ngrok: false`。

### 4. 获取访问令牌 (Obtain Access Token)

- 运行 `python src/auth_manager.py` 脚本。
- 脚本会自动打开浏览器，引导你完成 Schwab 账户授权流程。
- 授权成功后，脚本会自动获取访问令牌并保存到 `schwabs_token.json` 文件中。此文件已自动添加到 `.gitignore`。

### 5. 运行 (Usage)

- **测试 Schwab API 客户端:**
    - 运行 `python src/schwab_api.py` 脚本。
    - 脚本将加载已保存的令牌，并尝试获取你的 Schwab 账户信息（包括持仓），并在控制台打印简洁的概览。
    - 此脚本也负责自动刷新和保存令牌。

## ⚠️ 免责声明 (Disclaimer)

**本项目仅为个人学习和研究目的，不构成任何投资建议。**

所有交易决策均由本程序的算法自动执行，可能存在无法预料的Bug、API延迟、网络问题或市场极端行情等风险。使用本项目可能导致您的投资本金发生亏损。

**使用者必须自行承担一切风险。作者不对任何因使用本软件而导致的任何形式的损失负责。**

**投资有风险，入市需谨慎。**

## 路线图 (Roadmap)

- [ ] 扩展 Schwab API 客户端功能，支持更多 Trader API 端点（如订单管理、行情数据）。
- [ ] 增加对 Schwab Market Data API 的支持。
- [ ] 优化错误处理和日志记录。
- [ ] 编写更全面的单元测试。

## 贡献 (Contributing)

欢迎提交 Pull Requests 或 Issues。对于重大更改，请先开一个 issue 进行讨论。

## 许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
