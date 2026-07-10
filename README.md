# 6hzs3.17 逆向工程

## 文件说明

| 文件 | 用途 |
|------|------|
| `native_launcher.py` | **原生修改启动器** - 只改验证服务器地址指向本地，其他代码零改动 |
| `run_cracked.py` | 完全绕过启动器 - 跳过所有许可证验证 |
| `bypass_license.py` | 许可证绕过补丁模块 |
| `TECHNICAL.md` | 完整逆向分析报告 |

## 原生修改（推荐）

打开 `native_launcher.py`，修改第 24 行的服务器地址：

```python
CUSTOM_SERVER_URL = "http://127.0.0.1:8080/api"  # 改成你的本地地址
```

然后运行：

```
C:\Python314\python.exe native_launcher.py
```

也可通过命令行参数指定：

```
C:\Python314\python.exe native_launcher.py --server http://你的地址:端口/api
```

## 架构分析

详见 [TECHNICAL.md](TECHNICAL.md)