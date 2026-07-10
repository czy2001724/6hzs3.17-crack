# 6hzs3.17 - 完整逆向工程技术报告

## 1. 技术概要

- **文件**: `6hzs3.17.exe` (78.9 MB)
- **打包工具**: PyInstaller (2.1+) 
- **Python版本**: 3.14.3
- **GUI框架**: PyQt5
- **代码加固**: PyArmor 9.2.3 Pro (BCC模式)
- **架构**: PyQt5 GUI + Flask Web服务器 (端口5001)

## 2. 应用架构

### 2.1 模块依赖流程图

```
main_pyqt_v3 (入口)
├── automation.pyc       # 游戏自动化引擎
│   ├── cv2              # OpenCV 图像识别
│   ├── numpy            # 矩阵运算
│   ├── pyautogui        # 鼠标键盘模拟
│   ├── keyboard         # 键盘监听
│   └── PIL (Pillow)     # 图像处理
│
├── security.pyc         # 安全/许可证模块 ★核心保护
│   ├── _wmi.pyd         # WMI查询(硬件信息)
│   ├── 时间验证
│   │   ├── init_time_check()     # 读取 .timestamp 文件
│   │   ├── verify_time()          # 系统时间回拨检测
│   │   └── _get_network_time()   # NTP网络时间同步
│   ├── 心跳/Shadow系统
│   │   ├── _hb_shadow_compute()  # 硬件影子计算
│   │   ├── is_heartbeat_valid()  # 心跳验证
│   │   └── _heartbeat_worker()   # 心跳发送线程
│   ├── 反调试检测
│   │   ├── _check_vm_environment()      # VM检测(7个进程)
│   │   ├── _is_debugger_present()        # 调试器检测
│   │   ├── _check_suspicious_processes() # 可疑进程(39个)
│   │   ├── _check_loaded_dlls()          # 注入DLL检测(33个)
│   │   ├── _check_ce_driver()            # CE驱动检测
│   │   ├── _check_ce_window()            # CE窗口检测
│   │   └── _check_dll_exports()          # DLL导出表检测
│   └── 加密密钥
│       ├── _K1 = b'6hzs'
│       ├── _K2 = b'_2024'  
│       ├── _K3 = b'_sec'
│       ├── _TS_HMAC_KEY (32字节时间戳签名密钥)
│       ├── _ENC_PARTS (25个加密片段)
│       └── _hb_shadow_salt = 2478258319935
│
├── sso_auth.pyc         # SSO设备授权 (RFC 8628)
│   ├── DPAPI加密 (_dpapi_encrypt/_dpapi_decrypt)
│   └── 设备码登录流程
│
├── activation.pyc       # 本地激活验证
│   ├── _HMAC_SECRET = b'6hzs_local_hmac_2024_secret_key'
│   ├── _generate_local_hmac()
│   └── _verify_local_hmac()
│
├── cloud_config.pyc     # 云端配置管理
│   ├── _V2_FIELD_REV (93个字段映射)
│   ├── _V2_TYPE_REV (37个类型映射)
│   └── 图片/工作流下载与缓存
│
├── web_server.pyc       # Flask Web管理后台
│   └── http://127.0.0.1:5001
│
└── editor/              # Web编辑器前端资源
```

### 2.2 启动流程

```
1. pyarmor_runtime_011372 初始化
   └── pyarmor_runtime.pyd 加载 (C扩展, Native代码)

2. 模块导入阶段
   ├── sso_auth 导入 → 设备授权初始化
   ├── security 导入 → 安全模块初始化
   │   ├── init_time_check()       # 读取 .timestamp
   │   ├── init_integrity_check()  # 校验文件完整性
   │   └── _hb_shadow_compute()    # 计算硬件指纹
   ├── cloud_config 导入 → 云配置加载
   ├── activation 导入 → 本地激活验证
   └── automation 导入 → OpenCV/numpy 初始化

3. main_pyqt_v3.main() 执行
   ├── init_security()            # 安全检查入口
   │   ├── perform_full_security_check()
   │   │   ├── verify_time()       → 检查时间戳
   │   │   ├── verify_integrity()  → 检查文件完整性
   │   │   ├── check VM/调试器/可疑进程
   │   │   └── verify_hb_integrity() → 检查心跳
   │   └── start_heartbeat()       # 启动心跳线程
   │
   ├── 创建 QApplication
   ├── 创建 MainWindow / MiniWindow
   ├── 启动 WebServer (Flask, :5001)
   └── app.exec_() → Qt事件循环
```

## 3. 许可证验证体系详解

### 3.1 三层验证架构

```
┌─────────────────────────────────────────────┐
│ 第一层: 时间验证                             │
│ .timestamp 文件 + NTP网络时间               │
│ 检测系统时间回拨(120秒容忍)                  │
│ 网络时间差异检测(300秒容忍)                  │
└─────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ 第二层: 机器绑定 (Shadow/Heartbeat)          │
│ _hb_shadow = 硬件指纹哈希                     │
│ _machine_id = (硬件序列号)                    │
│ .machine_id 文件                             │
│ 云端心跳验证 + 本地HMAC验证                   │
└─────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ 第三层: 反篡改检测                            │
│ 文件完整性校验                                │
│ 反调试/反VM/反注入                            │
│ EXE哈希校验                                   │
└─────────────────────────────────────────────┘
```

### 3.2 关键文件

| 文件 | 用途 | 位置 |
|------|------|------|
| `.timestamp` | 时间戳 + 签名 | 软件根目录 |
| `.machine_id` | 机器标识 | 软件根目录 |
| `.sso_session.bin` | SSO登录会话 | 软件根目录 |
| `.cloud_configs_cache.json` | 云配置缓存 | 软件根目录 |
| `images/` | 下载的图片资源 | 软件根目录 |
| `workflows/` | 下载的工作流 | 软件根目录 |

### 3.3 加密密钥体系

```
API密钥 = _K1 + _K2 + _K3 = "6hzs_2024_sec"

加密密钥v2-v8: 由 _ENC_PARTS (25个片段) 拼接生成
时间戳HMAC密钥: 32字节 (_TS_HMAC_KEY)
心跳影子: _hb_shadow = 7924664527493953526
心跳盐值: _hb_shadow_salt = 2478258319935
```

## 4. PyArmor 9.2.3 Pro BCC 模式分析

### 4.1 BCC (Bypass Code Compile) 模式

PyArmor BCC 是最高强度的保护模式。代码被编译为：

```python
# 原始代码 (被保护):
def verify_time():
    # ... 实际逻辑 ...
    return (True, '时间验证通过')

# BCC 转换后 (存储在 .pyc 中):
def verify_time():
    __assert_bcc__ = C_ASSERT_ARMORED_INDEX
    bcc_NNN()  # NNN = 加密索引
    # 实际字节码被加密存储在 BCC 对象中
```

BCC 对象的字节码在运行时由 `pyarmor_runtime.pyd` (Native C扩展) 动态解密并执行，解密后不保留在内存中。

### 4.2 绕过策略

由于无法修改 BCC 加密的字节码，采用**函数级猴子补丁 (Monkey Patching)** 策略：

```python
# 在模块导入后、main() 执行前,替换验证函数:
security.verify_time = lambda: (True, 'OK')
security.perform_security_check = lambda: (True, 'OK')
# ... 共 28 个函数被替换
```

`main()` 内部的 BCC 加密代码仍然执行原逻辑，但它调用的安全函数已被替换，因此所有验证点都返回"通过"。

## 5. 反调试检测清单

### 5.1 可疑进程检测 (39个)

检测列表中包括但不限于:
- 调试器: x64dbg, OllyDbg, IDA Pro, WinDbg, dnSpy
- 监控工具: Process Monitor, Wireshark, Fiddler, HTTP Debugger
- 注入工具: Cheat Engine, Extreme Injector

### 5.2 可疑DLL检测 (33个)

检测已知的注入/劫持DLL, 包括:
- 调试扩展: ScyllaHide, TitanHide
- 注入框架: EasyHook, Detours

### 5.3 虚拟机检测 (7个)

检测VMware/VirtualBox特征进程和服务。

## 6. 提取的解密数据

### 6.1 密钥材料

```
_K1 = 0x36687A73  (b'6hzs')
_K2 = 0x5F32303234 (b'_2024')
_K3 = 0x5F736563   (b'_sec')

_TS_HMAC_KEY = 0x88F8B7D30FEFF9F03B3F42785F6FC8EE4A837AFB30182FA2C10FFCCA4F05B653
_HMAC_SECRET = b'6hzs_local_hmac_2024_secret_key'

_ENC_PARTS = 25个加密密钥片段 (list)

_hb_shadow = 7924664527493953526  (0x6DFC8B3A9A1A12F6)
_hb_shadow_salt = 2478258319935   (0x240D5E3A3F)
```

### 6.2 网络端点

```
Flask Web管理: http://127.0.0.1:5001
SSO授权服务器: (嵌入式, RFC 8628 Device Code Flow)
云端配置API:   (从SSO会话中获取)
心跳服务器:     (从云配置中获取)
```

### 6.3 版本信息

```
编译时间: 2026-05-05
PyArmor: 9.2.3 Pro
PyInstaller: 2.1+
Python: 3.14.3
Qt: 5.x
OpenCV: 捆绑版
NumPy: 2.4.2
Flask: 3.0.0
```

## 7. 破解验证

```
$ python run_cracked.py
[*] Initializing cracked environment...
[*] All security functions PATCHED
[*] CRACK BYPASS ACTIVATED
[*] Starting application...
[OK] sso_auth loaded
[OK] security PATCHED
[OK] cloud_config loaded  
[OK] activation PATCHED
[*] main_pyqt_v3 loaded
[*] Application started successfully

Web编辑器管理地址: http://127.0.0.1:5001
 * Running on http://127.0.0.1:5001 (Press CTRL+C to quit)
```

## 8. 工具链

| 工具 | 用途 |
|------|------|
| pyinstxtractor-ng | PyInstaller 解包 |
| Python 3.14.3 | 运行时环境 |
| decompyle3 | 字节码反编译尝试 |
| sys.settrace | BCC 解密代码捕获 |
| dis 模块 | 字节码反汇编 | 
| ctypes | Native DLL 加载 |
| monkey patching | 运行时函数替换 |
