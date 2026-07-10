# 6hzs3.17 完整逆向工程

## 项目结构

```
├── README.md                  # 本文件
├── TECHNICAL.md               # 完整逆向分析报告
├── API_PROTOCOL.md            # 验证服务器 API 协议
│
├── native_launcher.py         # 原生修改启动器 (只改服务器地址)
├── bypass_license.py          # 许可证绕过补丁模块
├── run_cracked_final.py       # 完全绕过启动器
│
├── extract_config.py          # 配置密钥提取工具
├── capture_traffic3.py        # HTTP 流量抓包工具
└── mock_server.py             # 本地模拟验证服务器
```

## 技术概要

| 项目 | 详情 |
|------|------|
| 文件 | `6hzs3.17.exe` (78.9 MB) |
| 打包 | PyInstaller 2.1+ |
| Python | 3.14.3 |
| GUI | PyQt5 |
| 加固 | PyArmor 9.2.3 Pro (BCC 模式) |
| 架构 | PyQt5 GUI + Flask Web (5001端口) |

## 快速使用

### 改服务器地址（推荐）

编辑 `native_launcher.py` 第 24 行：
```python
CUSTOM_SERVER_URL = "http://你的地址:端口/api"
```
然后运行：
```
C:\Python314\python.exe native_launcher.py
```

### 本地模拟服务器

```
C:\Python314\python.exe mock_server.py
```

### 抓取 HTTP 流量

```
C:\Python314\python.exe capture_traffic3.py
```

## 模块架构

```
main_pyqt_v3 (入口)
├── automation.pyc       # 游戏自动化引擎 (OpenCV/numpy/PyAutoGUI)
├── security.pyc         # 安全许可证模块 ★
│   ├── 时间验证 (.timestamp + NTP)
│   ├── 心跳系统 (POST /api/heartbeat)
│   └── 反调试检测 (VM/调试器/注入DLL/CE)
├── sso_auth.pyc         # SSO 设备授权 (RFC 8628 + DPAPI)
├── activation.pyc       # 本地激活验证 (HMAC)
├── cloud_config.pyc     # 云端配置管理
└── web_server.pyc       # Flask Web 管理 (http://127.0.0.1:5001)
```

## 验证服务器 API

### POST /api/heartbeat
```
请求: {"machine_id": "xxx", "password": "DFJHj4RThBGDdj23w122DOUD2", "version": "2.28"}
响应: (在 BCC 加密层, 需运行时抓包)
```

### 密钥材料

```
_K1 + _K2 + _K3 = "6hzs_2024_sec"
_TS_HMAC_KEY = 88f8b7d30feff9f03b3f42785f6fc8ee4a83... (32 bytes)
_HMAC_SECRET = "6hzs_local_hmac_2024_secret_key"
_hb_shadow = 7106634142735222219
_hb_shadow_salt = 2053431851807
```

### 反调试清单

- 虚拟机检测: 7 个进程特征
- 可疑进程检测: 39 个进程名
- 可疑DLL检测: 33 个 DLL 名
- CE 驱动/窗口检测
- DLL 导出表检测

详见 [TECHNICAL.md](TECHNICAL.md)

## 工具链

| 工具 | 用途 |
|------|------|
| pyinstxtractor-ng | PyInstaller 解包 |
| Python 3.14.3 | 运行时环境 |
| decompyle3 | 字节码反编译 |
| sys.settrace | BCC 解密代码追踪 |
| dis | 字节码反汇编 |

## 免责声明

本项目仅供软件逆向工程研究和技术学习使用。
