"""
6hzs3.17 - 原生修改启动器
====================
不 patch 任何安全函数，仅修改验证服务器地址指向你自己的服务器。

用法:
    C:\Python314\python.exe native_launcher.py --server http://你的本地地址:端口/api

或在文件里改 SERVER_URL 变量后直接运行。

原理:
    在 main() 调用 init_security() / ActivationManager() / start_heartbeat() 时
    传入自定义 server_url，其余代码原封不动。
"""

import sys, os

# ============================================
# ★ 在这里改成你的本地服务器地址 ★
# ============================================
CUSTOM_SERVER_URL = "http://127.0.0.1:8080/api"
CUSTOM_SSO_URL = None     # None = 使用原地址
CUSTOM_PZWZ_URL = None    # None = 使用原地址
# ============================================

EXTRACTED_DIR = r'C:\Users\yan\Desktop\新建文件夹\extracted_src\6hzs3.17_copy.exe_extracted'
PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = r'C:\Python314'
APP_DIR = r'C:\Users\yan\Desktop\新建文件夹'

# 命令行参数覆盖
if '--server' in sys.argv:
    idx = sys.argv.index('--server')
    if idx + 1 < len(sys.argv):
        CUSTOM_SERVER_URL = sys.argv[idx + 1]

os.environ['QT_PLUGIN_PATH'] = os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins', 'platforms')
os.chdir(APP_DIR)

sys.path.insert(0, EXTRACTED_DIR)
sys.path.insert(1, PYZ_DIR)
for d in [EXTRACTED_DIR, PYTHON_DIR, os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'bin')]:
    if os.path.isdir(d):
        try: os.add_dll_directory(d)
        except: pass

sys.frozen = True
sys._MEIPASS = EXTRACTED_DIR
os.environ['_MEIPASS'] = EXTRACTED_DIR

import importlib
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')

# 只改 URL 相关的函数调用参数，其他零改动
import security
import activation
import sso_auth

# 保存原始函数引用
_orig_init_security = security.init_security
_orig_start_heartbeat = security.start_heartbeat
_orig_ActivationManager = activation.ActivationManager
_orig_SSOAuth = sso_auth.SSOAuth

# 替换为带自定义 URL 的版本
def _new_init_security(server_url=None, machine_id=None):
    return _orig_init_security(
        server_url=CUSTOM_SERVER_URL,
        machine_id=machine_id
    )

def _new_start_heartbeat(server_url=None, machine_id=None, interval=600):
    return _orig_start_heartbeat(
        server_url=CUSTOM_SERVER_URL,
        machine_id=machine_id or 'custom',
        interval=interval
    )

class _NewActivationManager(_orig_ActivationManager):
    def __init__(self, server_url=None, *args, **kwargs):
        super().__init__(
            server_url=CUSTOM_SERVER_URL,
            *args, **kwargs
        )

class _NewSSOAuth(_orig_SSOAuth):
    def __init__(self, client_id=None, sso_url=None, pzwz_url=None, *args, **kwargs):
        super().__init__(
            client_id=client_id,
            sso_url=CUSTOM_SSO_URL or sso_url,
            pzwz_url=CUSTOM_PZWZ_URL or pzwz_url,
            *args, **kwargs
        )

security.init_security = _new_init_security
security.start_heartbeat = _new_start_heartbeat
activation.ActivationManager = _NewActivationManager
sso_auth.SSOAuth = _NewSSOAuth

print(f"[*] 验证服务器 -> {CUSTOM_SERVER_URL}")
print(f"[*] 启动应用...")
print(f"[*] 不要关闭此窗口")
print()

import main_pyqt_v3
if hasattr(main_pyqt_v3, 'main'):
    main_pyqt_v3.main()

try:
    from PyQt5.QtWidgets import QApplication
    app = QApplication.instance()
    if app:
        app.exec_()
except:
    pass
