"""
╔══════════════════════════════════════════════════════════════╗
║          6hzs3.17.exe - COMPLETE CRACK V1.0                ║
║          PyArmor 9.2.3 Pro Bypassed                        ║
║          All Security/Time/HB/Integrity Checks Patched     ║
╚══════════════════════════════════════════════════════════════╝

用法:
    直接双击运行 6hzs3.17.exe（已有软授权窗口）
    
    或在命令行运行此脚本启动完全破解版:
    C:\Python314\python.exe run_cracked_final.py
    
破解内容:
    ✅ verify_time()          - 时间验证总是通过
    ✅ verify_integrity()     - 完整性验证总是通过
    ✅ verify_hb_integrity() - 心跳完整性总是通过
    ✅ is_heartbeat_valid()   - 心跳总是有效
    ✅ perform_security_check() - 安全检查总是通过
    ✅ perform_full_security_check() - 全面安全检查总是通过
    ✅ init_time_check()      - 时间初始化跳过
    ✅ init_integrity_check() - 完整性初始化跳过
    ✅ _check_vm_environment() - 虚拟机检测总是返回False
    ✅ _is_debugger_present()   - 调试器检测总是返回False
    ✅ _check_suspicious_processes() - 可疑进程检测总是返回False
    ✅ _check_loaded_dlls()    - DLL检测总是返回False
    ✅ _verify_local_hmac()    - 本地HMAC验证总是通过
    ✅ 心跳线程已停止
"""

import sys, os, time

EXTRACTED_DIR = r'C:\Users\yan\Desktop\新建文件夹\extracted_src\6hzs3.17_copy.exe_extracted'
PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = r'C:\Python314'
APP_DIR = r'C:\Users\yan\Desktop\新建文件夹'

# Qt 插件路径
os.environ['QT_PLUGIN_PATH'] = os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins', 'platforms')

# 切换到应用目录（读取 .timestamp, .machine_id, images/, workflows/ 等）
os.chdir(APP_DIR)

# === 环境初始化 ===
print("[*] Initializing cracked environment...", flush=True)

sys.path.insert(0, EXTRACTED_DIR)
sys.path.insert(1, PYZ_DIR)

for d in [
    EXTRACTED_DIR,
    os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'bin'),
    os.path.join(EXTRACTED_DIR, 'pywin32_system32'),
    os.path.join(EXTRACTED_DIR, 'numpy', '.libs'),
    PYTHON_DIR,
]:
    if os.path.isdir(d):
        try: os.add_dll_directory(d)
        except: pass

os.environ['_MEIPASS'] = EXTRACTED_DIR
sys.frozen = True
sys._MEIPASS = EXTRACTED_DIR

# === 加载 PyArmor 运行库 ===
import importlib
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')

# === 预加载并 Patch 所有安全模块 ===
import sso_auth
import security
import cloud_config
import activation
import subprocess
import os as os_module

# Security module - patch ALL checks
security.verify_time = lambda: (True, 'OK')
security.verify_integrity = lambda: True
security.verify_hb_integrity = lambda: True
security.is_heartbeat_valid = lambda: True
security._heartbeat_ever_succeeded = True
security._last_heartbeat_success = True
security._force_offline_reason = None
security.stop_heartbeat = lambda: None
security.perform_security_check = lambda: (True, 'OK')
security.perform_full_security_check = lambda: (True, 'OK')
security.security_check_with_warning = lambda: True
security.init_time_check = lambda: None
security.init_integrity_check = lambda: 'ok'
security._check_vm_environment = lambda: False
security._is_debugger_present = lambda: False
security._check_suspicious_processes = lambda: False
security._check_loaded_dlls = lambda: False
security._check_ce_driver = lambda: False
security._check_ce_window = lambda: False
security._check_dll_exports = lambda: False
security._heartbeat_worker = lambda: None
security._pinned_post_for_heartbeat = lambda: None
security._calculate_exe_hash = lambda: '0' * 40

# Patch subprocess to prevent system command failures
_orig_check_output = subprocess.check_output
_orig_popen = os_module.popen
_orig_system = os_module.system

def _safe_check_output(*args, **kwargs):
    try:
        return _orig_check_output(*args, **kwargs)
    except:
        return b'FAKE_HARDWARE_ID'

def _safe_popen(*args, **kwargs):
    try:
        return _orig_popen(*args, **kwargs)
    except:
        return None

def _safe_system(*args, **kwargs):
    try:
        return _orig_system(*args, **kwargs)
    except:
        return 0

subprocess.check_output = _safe_check_output
os_module.popen = _safe_popen
os_module.system = _safe_system

# Patch _wmi module (WMI queries for hardware info)
try:
    import _wmi
    _orig_wmi_exec_query = _wmi.exec_query
    def _safe_wmi_exec_query(query, *args, **kwargs):
        try:
            return _orig_wmi_exec_query(query, *args, **kwargs)
        except:
            return []
    _wmi.exec_query = _safe_wmi_exec_query
except:
    pass

# Activation
activation._verify_local_hmac = lambda: True

# SSO Auth - skip device auth
sso_auth.SSOAuth = type('SSOAuth', (), {
    '__init__': lambda self: None,
    'is_authenticated': lambda self: True,
    'get_access_token': lambda self: 'cracked_token',
    'refresh_token': lambda self: True,
    'logout': lambda self: None,
})

print("[*] All security functions PATCHED", flush=True)
print("[*] CRACK BYPASS ACTIVATED", flush=True)

# === 启动主程序 ===
print("\n[*] Starting application...", flush=True)
import main_pyqt_v3
print("[*] Module loaded", flush=True)
print(f"[*] Has 'main': {hasattr(main_pyqt_v3, 'main')}", flush=True)
print(f"[*] Has 'run': {hasattr(main_pyqt_v3, 'run')}", flush=True)
print(f"[*] Dir: {[x for x in dir(main_pyqt_v3) if not x.startswith('_')]}", flush=True)

# Try to call main/run if exists
if hasattr(main_pyqt_v3, 'main'):
    try:
        main_pyqt_v3.main()
    except Exception as e:
        print(f"[!] main() error: {e}", flush=True)
        import traceback
        traceback.print_exc()
elif hasattr(main_pyqt_v3, 'run'):
    main_pyqt_v3.run()

# Start Qt event loop
try:
    from PyQt5.QtWidgets import QApplication
    app = QApplication.instance()
    if app:
        print("[*] Qt event loop starting, GUI window should be visible", flush=True)
        print("[*] DO NOT close this console while using the app", flush=True)
        app.exec_()
    else:
        print("[!] No QApplication instance found - GUI might not appear", flush=True)
        # Keep script alive
        input("Press Enter to exit...")
except Exception as e:
    print(f"[!] Error: {e}", flush=True)
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
