# SchwabGridTrader

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-green.svg)

An automated quantitative trading bot for implementing cyclical grid trading strategies on the Charles Schwab platform via its official API.

一个基于嘉信理财 (Charles Schwab) 官方API的自动化量化交易机器人，用于实现周期性网格交易策略。

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

- **对接嘉信理财API:** 安全、可靠地进行账户授权和交易执行。
- **高度可配置:**
    - 交易标的 (Ticker Symbol)
    - 价格上轨/下轨 (Price Range Upper/Lower Bound)
    - 网格数量 (Number of Grids)
    - 单网格交易金额/数量 (Amount/Quantity per Grid)
    - 交易周期 (Trading Cycle)
- **自动化执行:** 启动后7x24小时监控行情（根据市场交易时间），自动下单，无需人工干预。
- **状态持久化:** 记录当前的持仓和网格状态，即使程序重启也能恢复。
- **详细日志:** 记录每一笔交易决策、API请求和执行结果，方便复盘和排错。

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

### 3. 配置 (Configuration)

1.  复制配置文件模板:
    ```bash
    cp config.example.yaml config.yaml
    ```

2.  编辑 `config.yaml` 文件，填入你的个人信息和策略参数：
    ```yaml
    # Schwab API Credentials
    api_key: "YOUR_APP_KEY"
    api_secret: "YOUR_APP_SECRET"
    # The callback url you set in your Schwab App settings
    callback_url: "https://127.0.0.1" 

    # Trading Strategy Settings
    # Repeat for each stock you want to trade
    strategies:
      - symbol: "AAPL"          # 交易标的
        enabled: true           # 是否启用此策略
        price_lower_bound: 150.0  # 价格区间下轨
        price_upper_bound: 180.0  # 价格区间上轨
        grid_quantity: 10         # 网格数量
        order_amount: 500.0       # 每格买入的金额 (美元)
        # Optional: cycle_days: 7  # 交易周期（天），可用于未来功能
    ```
    **注意:** `config.yaml` 包含敏感信息，切勿提交到你的Git仓库！`.gitignore` 文件已默认包含此规则。

### 4. 运行 (Usage)

1.  **首次运行获取Token:**
    首次运行需要进行OAuth授权，程序会自动打开浏览器，请登录并授权，然后将跳转后的URL粘贴回控制台。
    ```bash
    python main.py
    ```
    程序会自动保存 `token` 文件供后续使用。

2.  **开始交易:**
    之后再次运行，程序将自动加载 `token` 并开始监控和交易。
    ```bash
    python main.py
    ```

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
