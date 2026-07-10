"""
6hzs3.17 破解启动器
==================
将本文件与 bypass_license.py 放置于软件根目录（与 6hzs3.17.exe 同级）运行。

用法:
    C:\Python314\python.exe run_cracked.py

原理:
    在应用启动前将 28 个安全验证函数替换为空壳，使许可证检查永远返回"通过"。
    PyArmor 9.2.3 Pro BCC 加密的 main() 内部代码保持不变，但它调用的验证函数已全部被替换。
"""

import sys, os

# === 路径自动检测 ===
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRACTED_DIR = os.path.join(SCRIPT_DIR, 'extracted_src', '6hzs3.17_copy.exe_extracted')

if not os.path.isdir(EXTRACTED_DIR):
    print("[!] 请先将 6hzs3.17.exe 解包到 extracted_src/ 目录")
    print("[!] 使用: pyinstxtractor-ng 6hzs3.17.exe")
    sys.exit(1)

PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = os.path.dirname(sys.executable)

# === 环境初始化 ===
print("[*] Initializing cracked environment...", flush=True)

sys.path.insert(0, EXTRACTED_DIR)
sys.path.insert(1, PYZ_DIR)

os.environ['QT_PLUGIN_PATH'] = os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    EXTRACTED_DIR, 'PyQt5', 'Qt5', 'plugins', 'platforms'
)

for d in [
    EXTRACTED_DIR,
    os.path.join(EXTRACTED_DIR, 'PyQt5', 'Qt5', 'bin'),
    os.path.join(EXTRACTED_DIR, 'pywin32_system32'),
    PYTHON_DIR,
]:
    if os.path.isdir(d):
        try:
            os.add_dll_directory(d)
        except Exception:
            pass

os.environ['_MEIPASS'] = EXTRACTED_DIR
sys.frozen = True
sys._MEIPASS = EXTRACTED_DIR
os.chdir(SCRIPT_DIR)

# === 加载 PyArmor 运行时并 Patch ===
import importlib
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')

# 导入并 Patch 所有安全模块
import bypass_license as bypass
bypass.patch_all()

# === 启动主程序 ===
print("\n[*] Launching application...", flush=True)
import main_pyqt_v3

if hasattr(main_pyqt_v3, 'main'):
    main_pyqt_v3.main()

# 启动 Qt 事件循环
try:
    from PyQt5.QtWidgets import QApplication
    app = QApplication.instance()
    if app:
        print("[*] GUI window should be visible", flush=True)
        print("[*] 不要关闭此窗口, 关闭将退出程序", flush=True)
        app.exec_()
except Exception as e:
    print(f"[!] Qt event loop error: {e}", flush=True)
    input("Press Enter to exit...")
