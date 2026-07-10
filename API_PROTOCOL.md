# 验证服务器 API 协议

## 已知信息

验证服务器地址: `https://6hzszdh.isi.ink:49897/api`

## 已确认的 API 端点

### POST /api/heartbeat

心跳验证请求，由 security 模块的后台线程定期发送。

**请求:**
```json
{
    "machine_id": "eb8bbfcb994dd043:9cfe997eaa9cb644",
    "password": "DFJHj4RThBGDdj23w122DOUD2",
    "version": "2.28"
}
```

**响应格式:** (在 PyArmor BCC 加密层中, 需运行时抓包)

推测响应字段 (根据函数签名和 docstring):
- `status`: "ok" / "error"
- 可能包含签名验证字段 (函数 `_verify_heartbeat_signature` 存在)
- 可能包含 `next_interval`: 下次心跳间隔 (默认 600s)

### 推测的其他端点

根据模块结构和函数签名:

- `POST /api/verify` - 验证请求 (security.perform_security_check)
- `POST /api/activate` - 激活请求 (activation.ActivationManager)
- `POST /api/config` - 云配置下载 (cloud_config)
- SSO OAuth2 端点 (sso_auth, RFC 8628 Device Code Flow)

## 如何抓取完整协议

1. 启动本地模拟服务器:
   ```
   C:\Python314\python.exe mock_server.py
   ```

2. 用抓包脚本连接本地服务器:
   ```
   C:\Python314\python.exe capture_traffic3.py
   ```

3. 查看 `http_traffic.jsonl` 和 `server_log.jsonl` 获取完整请求/响应

## 搭建本地服务器

`native_launcher.py` 可将所有 API 请求重定向到你的本地服务器:
```python
CUSTOM_SERVER_URL = "http://127.0.0.1:8080/api"
```

参考 `mock_server.py` 了解基本响应格式。
