# SchwabGridTrader 开发约定

Charles Schwab API 集成模块，提供 OAuth 2.0 认证、令牌管理和基础交易 API 客户端。

## 技术栈

- **语言**: Python 3.8+
- **认证**: OAuth 2.0 Authorization Code Flow (PKCE)
- **API**: Schwab Trader API, Market Data API
- **状态**: 早期开发

## 项目结构

```
src/
  auth_manager.py   # OAuth2 认证和令牌管理
  schwab_api.py     # Schwab API 客户端
docs/               # Schwab API 参考文档
```

## 开发命令

```bash
# 安装依赖
pip install -r requirements.txt

# OAuth2 认证 (获取 token)
python src/auth_manager.py

# 测试 API 连接
python src/schwab_api.py
```

## 环境变量

见 `.env.example`，关键变量:
- `SCHWAB_APP_KEY` / `SCHWAB_APP_SECRET`: Schwab Developer Portal 凭证
- `SCHWAB_REDIRECT_URI`: OAuth 回调地址 (本地开发用 `https://127.0.0.1:8080/callback`)

## 安全注意事项

- 本仓库是 **PUBLIC**，提交前务必检查无敏感信息
- `schwabs_token.json` 已在 `.gitignore` 中排除
- API 凭证只通过 `.env` 管理

## 跨 Workspace 关联

| 关联项目 | 所在 Workspace | 关系 |
|----------|---------------|------|
| moomoo_custom_strategies | finance-trading | 同 workspace 内另一个交易平台项目，独立运作 |
