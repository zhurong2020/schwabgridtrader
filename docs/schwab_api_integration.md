# Schwab API 对接指南 for Grid Trading Tool

## 1. 引言

本指南旨在详细阐述 Schwab API 在 Grid Trading Tool 应用程序中的集成方案。通过此次集成，Grid Trading Tool 将扩展其券商对接能力，使用户能够直接通过应用程序管理 Schwab 账户、获取实时数据并执行交易，类似于现有对 Moomoo API 的支持。

## 2. 已实现的 Schwab API 功能概述

当前已开发的 Schwab API 模块（主要涉及 `src/auth_manager.py` 和 `src/schwab_api.py`）为与 Schwab Trader API 进行安全、认证的交互奠定了基础。已实现的核心功能包括：

*   **OAuth 2.0 授权码流程 (Authorization Code Flow) 与 PKCE 支持：**
    *   实现了 Schwab API 所要求的 OAuth 2.0 三方授权流程，确保用户认证和授权过程的安全性。
    *   集成了 PKCE (Proof Key for Code Exchange) 扩展，为公共客户端提供了额外的安全层。
    *   支持在本地开发环境（如 WSL）中启动 **本地 HTTPS 回调服务器**，用于接收 OAuth 回调，从而避免了对公共隧道服务（如 ngrok 免费版）的依赖，简化了开发调试流程。
*   **令牌管理：**
    *   自动获取、存储和刷新 Access Token (访问令牌) 和 Refresh Token (刷新令牌)。
    *   令牌凭据安全地存储在本地文件 `schwabs_token.json` 中，并已配置 `.gitignore` 确保其不会被提交到版本控制系统。
    *   Access Token 有效期为 30 分钟，Refresh Token 有效期为 7 天。`requests_oauthlib` 库已配置为自动处理令牌刷新，并在刷新后更新本地存储。
*   **基本账户信息检索：**
    *   能够获取用户关联的所有 Schwab 账户的哈希 ID 列表。
    *   能够根据账户哈希 ID 检索特定账户的详细信息，包括持仓 (positions) 等。

## 3. Grid Trading Tool 架构中的集成策略

为了将 Schwab API 无缝集成到 Grid Trading Tool 中，我们建议沿用现有 Moomoo 集成的模式，主要利用 `src/api_interface.py` 和 `src/api_manager.py` 模块。

*   **`src/config.py` & `config.ini`：**
    *   在 `config.ini` 中引入一个新的配置节（例如 `[SchwabAPI]`），用于存储 Schwab 相关的凭据和设置，包括：
        *   `client_id` (应用程序密钥)
        *   `client_secret` (应用程序秘密)
        *   `callback_url` (OAuth 回调 URL，例如 `https://127.0.0.1:5000`)
        *   `local_server_host` (本地回调服务器监听地址，例如 `127.0.0.1`)
        *   `local_server_port` (本地回调服务器监听端口，例如 `5000`)
        *   `auth_timeout` (授权超时时间，单位秒)
        *   `use_ngrok` (布尔值，指示是否使用 ngrok，默认为 `false`)
    *   `src/config.py` 需要更新以加载和解析这些新的 Schwab 配置项。
*   **`src/api_manager.py`：**
    *   此模块应扩展以管理 Schwab API 客户端实例。它将负责初始化 Schwab API 客户端、处理认证状态，并为 Schwab 特定的功能提供统一的接口。
    *   它将封装 `src/schwab_api.py` 中定义的 `SchwabAPI` 类实例。
    *   当 Schwab 令牌不可用或过期时，`api_manager.py` 将协调调用 `auth_manager.py` 中的 OAuth 流程。
*   **`src/api_interface.py`：**
    *   此模块应定义所有券商 API（Moomoo、Schwab 等）的通用接口。
    *   应在此处定义抽象方法，例如 `authenticate()`、`get_account_info()`、`get_positions()`、`place_order()`、`get_historical_orders()` 等。
    *   为 Schwab API 添加具体的实现类（例如 `SchwabAPIAdapter`），该类将调用 `api_manager.py` 中管理的 Schwab 特定方法。
*   **`src/auth_manager.py` (现有模块)：**
    *   此模块将作为独立的 OAuth 流程工具，负责启动本地 HTTPS 服务器、处理 Schwab 的回调、获取授权码并交换 Access Token 和 Refresh Token。它将被 `api_manager.py` 或 `schwab_api.py` 在需要新令牌时调用。
*   **`src/schwab_api.py` (现有模块)：**
    *   此模块将作为低级别的 Schwab API 客户端，负责处理直接的 API 请求、令牌的自动刷新和保存，以及对 API 响应的初步解析。它将由 `api_manager.py` 实例化和使用。

## 4. Schwab API 技术细节

*   **OAuth 2.0 授权流程：** Schwab 采用带有 PKCE 的三方授权码流程。
    *   **授权 URL：** `https://api.schwabapi.com/v1/oauth/authorize`
    *   **令牌 URL：** `https://api.schwabapi.com/v1/oauth/token`
    *   **`redirect_uri`：** 必须是 **HTTPS** URL。对于本地开发，强烈推荐使用 `https://127.0.0.1:PORT`。此 URL 必须在 Schwab 开发者门户和应用程序的 `config.ini` 中精确配置，包括协议、IP 地址和端口号。
    *   **`scope`：** 通用 API 访问所需的 `scope` 为 `"api"`。在授权请求和令牌交换过程中，此 `scope` 必须保持一致。
    *   **PKCE：** 授权请求中必须包含 `code_challenge` 和 `code_challenge_method=S256`。令牌交换时需要 `code_verifier`。
*   **令牌存储：** Access Token 和 Refresh Token 存储在项目根目录的 `schwabs_token.json` 文件中。此文件包含敏感信息，**绝不能**提交到版本控制系统。
*   **令牌刷新：** Access Token 有效期较短（30 分钟）。Refresh Token（7 天有效期）用于在 Access Token 过期后获取新的 Access Token，而无需用户重新进行完整的认证流程。`requests_oauthlib.OAuth2Session` 已配置为自动处理令牌刷新和保存。
*   **API 端点 (Trader API)：**
    *   **获取账户哈希 ID：** `https://api.schwabapi.com/trader/v1/accounts/accountNumbers`
    *   **获取账户详细信息：** `https://api.schwabapi.com/trader/v1/accounts/{accountHash}`。此端点支持 `fields` 参数，可用于请求特定类型的数据（例如 `positions`、`balances`）。
*   **错误处理：** API 响应应检查 HTTP 状态码（例如使用 `response.raise_for_status()`）并解析响应体以获取具体的错误消息。

## 5. 高级实现步骤 (High-Level Implementation Steps)

1.  **更新 `config.ini` 和 `src/config.py`：**
    *   在 `config.ini` 中添加 `[SchwabAPI]` 配置节，并填充必要的 Schwab API 凭据和回调设置。
    *   修改 `src/config.py` 以加载和提供这些新的 Schwab 配置。
2.  **将 `auth_manager.py` 集成到 `api_manager.py` (或新的 `schwab_auth.py`)：**
    *   `auth_manager.py` 中的 `get_new_token()` 函数将作为启动 OAuth 流程的入口点，当 Schwab 令牌不存在或无效时被调用。
    *   如果认证逻辑变得复杂，可以考虑创建一个独立的 `src/schwab_auth.py` 模块来封装 `auth_manager.py` 的功能。
3.  **将 `src/schwab_api.py` 封装为专用的 Schwab 客户端：**
    *   确保 `SchwabAPI` 类是健壮的，并处理所有 Schwab 特定的 API 调用。
    *   它应通过 `api_manager.py` 从 `src/config.py` 获取配置（Client ID、Secret 等）。
4.  **扩展 `src/api_manager.py`：**
    *   添加一个方法（例如 `get_schwab_client()`），该方法返回一个已初始化并准备好使用的 `SchwabAPI` 实例。
    *   此方法应检查现有令牌，如果未找到，则触发通过 `auth_manager.py` 进行的 OAuth 流程。
    *   实现诸如 `query_schwab_accounts()`、`query_schwab_positions()`、`place_schwab_order()` 等方法，这些方法内部将调用 `SchwabAPI` 客户端。
5.  **更新 `src/api_interface.py`：**
    *   定义通用券商操作的抽象方法。
    *   创建一个 `SchwabAPIAdapter` 类，该类实现 `api_interface` 中定义的抽象方法，并使用 `api_manager.py` 中提供的 Schwab 特定方法。
6.  **修改 `src/gui.py`：**
    *   在用户界面中添加新的元素（例如，“连接 Schwab 账户”按钮）以启动 OAuth 流程。
    *   添加按钮/字段以触发 Schwab 特定的查询（例如，“查询 Schwab 资金”、“查询 Schwab 持仓”）。
    *   确保 GUI 能够正确显示 Schwab 特定的账户和持仓数据。
7.  **错误处理和日志记录：** 为 API 调用和认证失败实现健壮的错误处理。将这些错误信息集成到应用程序的日志系统中。

## 6. 在 Grid Trading Tool 中的使用

*   **配置：** 用户将在 `config.ini` 中配置其 Schwab API 凭据和回调 URL。
*   **认证：** GUI 中的新按钮（例如，“连接 Schwab 账户”）将启动基于浏览器的 OAuth 流程。成功完成后，令牌将安全地保存到本地。
*   **账户查询：** 新的按钮（例如，“查询 Schwab 资金”、“查询 Schwab 持仓”、“查询 Schwab 历史订单”）将调用 `api_manager.py` 中相应的方法（通过 `api_interface.py`）来获取和显示 Schwab 账户数据。
*   **订单下达：** “根据计划下达订单”功能将扩展，允许用户选择券商（Moomoo 或 Schwab），然后使用相应的 API 适配器在 Schwab 上执行交易。

## 7. 重要注意事项

*   **安全性：** `schwabs_token.json` 文件绝不能提交到版本控制系统。务必强调 API 密钥和秘密的安全处理。
*   **Schwab 开发者门户配置：** Schwab 开发者门户中的 `Callback URL` 必须与 `config.ini` 中配置的 `callback_url` 精确匹配。
*   **自签名证书：** 对于本地 HTTPS 开发，用户会遇到浏览器关于自签名证书的警告。应在应用程序的文档中提供绕过这些警告的说明。
*   **API 速率限制：** 在设计频繁的数据请求时，请注意 Schwab API 的速率限制。
*   **API 类型：** Schwab 拥有独立的市场数据 API 和交易 API。确保为每个目的使用正确的 API 端点。当前实现主要侧重于 Trader API。
*   **免责声明：** 再次强调与交易相关的财务风险以及本工具的教育性质。
