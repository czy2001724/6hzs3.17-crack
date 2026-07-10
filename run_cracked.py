"""
6hzs3.17 鐮磋В鍚姩鍣?==================
灏嗘湰鏂囦欢涓?bypass_license.py 鏀剧疆浜庤蒋浠舵牴鐩綍锛堜笌 6hzs3.17.exe 鍚岀骇锛夎繍琛屻€?
鐢ㄦ硶:
    C:\Python314\python.exe run_cracked.py

鍘熺悊:
    鍦ㄥ簲鐢ㄥ惎鍔ㄥ墠灏?28 涓畨鍏ㄩ獙璇佸嚱鏁版浛鎹负绌哄３锛屼娇璁稿彲璇佹鏌ユ案杩滆繑鍥?閫氳繃"銆?    PyArmor 9.2.3 Pro BCC 鍔犲瘑鐨?main() 鍐呴儴浠ｇ爜淇濇寔涓嶅彉锛屼絾瀹冭皟鐢ㄧ殑楠岃瘉鍑芥暟宸插叏閮ㄨ鏇挎崲銆?"""

import sys, os

# === 璺緞鑷姩妫€娴?===
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRACTED_DIR = os.path.join(SCRIPT_DIR, 'extracted_src', '6hzs3.17_copy.exe_extracted')

if not os.path.isdir(EXTRACTED_DIR):
    print("[!] 璇峰厛灏?6hzs3.17.exe 瑙ｅ寘鍒?extracted_src/ 鐩綍")
    print("[!] 浣跨敤: pyinstxtractor-ng 6hzs3.17.exe")
    sys.exit(1)

PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = os.path.dirname(sys.executable)

# === 鐜鍒濆鍖?===
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

# === 鍔犺浇 PyArmor 杩愯鏃跺苟 Patch ===
import importlib
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')

# 瀵煎叆骞?Patch 鎵€鏈夊畨鍏ㄦā鍧?import bypass_license as bypass
bypass.patch_all()

# === 鍚姩涓荤▼搴?===
print("\n[*] Launching application...", flush=True)
import main_pyqt_v3

if hasattr(main_pyqt_v3, 'main'):
    main_pyqt_v3.main()

# 鍚姩 Qt 浜嬩欢寰幆
try:
    from PyQt5.QtWidgets import QApplication
    app = QApplication.instance()
    if app:
        print("[*] GUI window should be visible", flush=True)
        print("[*] 涓嶈鍏抽棴姝ょ獥鍙? 鍏抽棴灏嗛€€鍑虹▼搴?, flush=True)
        app.exec_()
except Exception as e:
    print(f"[!] Qt event loop error: {e}", flush=True)
    input("Press Enter to exit...")
