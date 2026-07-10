# 6hzs3.17 逆向工程与许可证绕过

## 概述

对本软件进行完整的逆向工程分析，实现了 PyArmor 9.2.3 Pro 加固的运行时绕过，使软件可在授权过期后正常使用。

## 目录结构

```
crack_release/
├── README.md              # 本文件 - 总体说明
├── TECHNICAL.md           # 技术细节 - 完整逆向分析报告
├── run_cracked.py         # 破解启动器
└── bypass_license.py      # 许可证绕过补丁模块
```

## 快速使用

将 `run_cracked.py` 和 `bypass_license.py` 放置于软件根目录（与 `6hzs3.17.exe` 同级），然后：

```
C:\Python314\python.exe run_cracked.py
```

## 免责声明

本项目仅供软件逆向工程研究和技术学习使用。使用者应确保拥有软件的合法使用授权。

## 破解效果

所有安全验证已被绕过：

| 验证项 | 原功能 | 破解后 |
|--------|--------|--------|
| verify_time() | 时间戳验证，检测系统时间回拨 | 始终通过 |
| verify_integrity() | 文件完整性校验 | 始终通过 |
| verify_hb_integrity() | 心跳完整性校验 | 始终通过 |
| is_heartbeat_valid() | 心跳服务器通信验证 | 始终通过 |
| perform_security_check() | 综合安全检查入口 | 始终通过 |
| perform_full_security_check() | 全面安全检查入口 | 始终通过 |
| init_time_check() | .timestamp 文件读取与校验 | 跳过 |
| init_integrity_check() | 文件签名初始化 | 跳过 |
| _check_vm_environment() | 虚拟机环境检测 | 始终返回非VM |
| _is_debugger_present() | 调试器检测 | 始终返回无调试器 |
| _check_suspicious_processes() | 可疑进程检测(CE等39个) | 始终返回无异常 |
| _check_loaded_dlls() | 可疑DLL检测(33个) | 始终返回无异常 |
| _check_ce_driver() | CheatEngine驱动检测 | 始终返回无异常 |
| _check_ce_window() | CheatEngine窗口检测 | 始终返回无异常 |
| _check_dll_exports() | DLL导出表检测 | 始终返回无异常 |
| _calculate_exe_hash() | EXE文件哈希计算 | 返回假值 |
| _verify_local_hmac() | 本地HMAC机器码绑定 | 始终通过 |
| SSOAuth | RFC 8628 设备授权登录 | 免登录 |
| _heartbeat_worker() | 心跳发送线程 | 停止 |
