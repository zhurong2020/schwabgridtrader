# SchwabGridTrader

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-green.svg)

An automated quantitative trading bot for implementing cyclical grid trading strategies on the Charles Schwab platform via its official API, with robust OAuth 2.0 authentication and token management.

一个基于嘉信理财 (Charles Schwab) 官方API的自动化量化交易机器人，用于实现周期性网格交易策略，并具备强大的OAuth 2.0认证和令牌管理功能。

## 核心策略：周期网格 (Core Strategy: Cyclical Grid)

本项目的核心是**周期网格策略**。与传统网格策略不同，它结合了时间周期和价格区间：

1.  **定义周期 (Define Cycle):** 设定一个固定的交易周期，例如一周、一个月。
2.  **确定标的与区间 (Set Target & Range):** 选择一个你认为的优质标的（如某支股票或ETF），并为其估算一个在此周期内大概率会波动的价格区间（例如 $10.00 - $12.00）。
3.  **构建网格 (Build Grid):** 在价格区间内，自动生成一系列的买入和卖出点位。
4.  **自动交易 (Automated Trading):**
    *   当价格下跌触及某个买入网格线时，自动执行买入。
    *   当价格上涨触及一个已持仓成本之上的卖出网格线时，自动执行卖出，完成一轮套利。
5.  **周期重复 (Repeat):** 在一个周期结束后，可以根据市场情况重新评估和设定下一个周期的交易区间，不断重复获利。

这种策略旨在从标的物的区间震荡中持续获利，而不是赌单边上涨。

## 主要功能 (Key Features)

- **OAuth 2.0 认证与令牌管理:**
    - 实现与嘉信理财 API 的安全 OAuth 2.0 授权码流程，支持 PKCE。
    - 支持在本地开发环境（如 WSL）中启动 **本地 HTTPS 回调服务器**，简化调试。
    - 自动获取、存储和刷新 Access Token 和 Refresh Token，确保会话持久性。
    - 敏感令牌文件 `schwabs_token.json` 已自动添加到 `.gitignore`。
- **对接嘉信理财API:** 安全、可靠地进行账户授权和基本账户信息（如持仓）的获取。
- **高度可配置:**
    - 交易标的 (Ticker Symbol)
    - 价格上轨/下轨 (Price Range Upper/Lower Bound)
    - 网格数量 (Number of Grids)
    - 单网格交易金额/数量 (Amount/Quantity per Grid)
    - 交易周期 (Trading Cycle)
- **自动化执行:** 启动后7x24小时监控行情（根据市场交易时间），自动下单，无需人工干预。
- **状态持久化:** 记录当前的持仓和网格状态，即使程序重启也能恢复。
- **详细日志:** 记录每一笔交易决策、API请求和执行结果，方便复盘和排错.

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

- [ ] 实现更灵活的非对称网格策略
- [ ] 增加基于布林带或RSI指标动态调整价格区间的功能
- [ ] 开发简单的Web界面用于监控和管理
- [ ] 集成回测功能
- [ ] 支持更多交易品种（如期权）

## 贡献 (Contributing)

欢迎提交 Pull Requests 或 Issues。对于重大更改，请先开一个 issue 进行讨论。

## 许可证 (License)

本项目采用 [MIT License](LICENSE) 开源许可证。
