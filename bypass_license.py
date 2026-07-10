"""
6hzs3.17.exe LICENSE BYPASS PATCHER

Analysis of license system:
- security.verify_time() -> (bool, str) - time validation
- security.verify_integrity() -> bool - file integrity check  
- security.verify_hb_integrity() -> bool - heartbeat integrity
- security.is_heartbeat_valid() -> bool - heartbeat status
- security.perform_security_check() -> (bool, str) - main security check
- security.perform_full_security_check() -> (bool, str) - full security check
- security.init_time_check() -> None - initializes time check (reads .timestamp)
- security.init_integrity_check() -> str - initializes integrity check
- security.stop_heartbeat() -> None - stops heartbeat thread
- activation._verify_local_hmac() -> bool - local HMAC verification
- sso_auth - SSO device authorization

This script patches all security functions to always return success.
"""

import sys, os, importlib, types

EXTRACTED_DIR = r'C:\Users\yan\Desktop\新建文件夹\extracted_src\6hzs3.17_copy.exe_extracted'
PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = r'C:\Python314'

sys.path = [
    EXTRACTED_DIR, PYZ_DIR,
    os.path.join(PYTHON_DIR, 'Lib'),
    os.path.join(PYTHON_DIR, 'Lib', 'site-packages'),
    PYTHON_DIR,
    os.path.join(PYTHON_DIR, 'python314.zip'),
    os.path.join(PYTHON_DIR, 'DLLs'),
]

for d in [EXTRACTED_DIR, PYTHON_DIR]:
    if os.path.isdir(d):
        try: os.add_dll_directory(d)
        except: pass

# Load PyArmor
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')
print("PyArmor loaded")

# Import all target modules
import sso_auth
import security
import cloud_config
import activation

print("\n[*] Patching security module...")

# 1. Patch time checks
security.verify_time = lambda: (True, '时间验证通过')
print("  [OK] verify_time -> always True")

# 2. Patch integrity checks  
security.verify_integrity = lambda: True
security.verify_hb_integrity = lambda: True
security.init_integrity_check = lambda: 'integrity_ok'
print("  [OK] verify_integrity -> always True")

# 3. Patch heartbeat
security.is_heartbeat_valid = lambda: True
security._heartbeat_ever_succeeded = True
security._last_heartbeat_success = True
security._force_offline_reason = None
security.stop_heartbeat = lambda: None
print("  [OK] heartbeat -> always valid")

# 4. Patch security checks
security.perform_security_check = lambda: (True, '安全检测通过')
security.perform_full_security_check = lambda: (True, '全面安全检测通过')
security.security_check_with_warning = lambda: True
print("  [OK] security checks -> always pass")

# 5. Patch init functions
security.init_time_check = lambda: None
print("  [OK] init_time_check -> noop")

# 6. Patch anti-debug/VMs
security._check_vm_environment = lambda: False
security._is_debugger_present = lambda: False
security._check_suspicious_processes = lambda: False
security._check_loaded_dlls = lambda: False
security._check_ce_driver = lambda: False
security._check_ce_window = lambda: False
security._check_dll_exports = lambda: False
print("  [OK] anti-debug -> always clean")

# 7. Patch activation
activation._verify_local_hmac = lambda: True
print("  [OK] local HMAC -> always valid")

# 8. Patch heartbeat worker to do nothing
security._heartbeat_worker = lambda: None
security._pinned_post_for_heartbeat = lambda: None
print("  [OK] heartbeat worker -> noop")

print("\n[*] All security functions patched!")
print("[*] The application should now run without license checks")
print()

# Verify the patches
print("[*] Verification:")
print(f"  verify_time(): {security.verify_time()}")
print(f"  verify_integrity(): {security.verify_integrity()}")
print(f"  perform_security_check(): {security.perform_security_check()}")
print(f"  is_heartbeat_valid(): {security.is_heartbeat_valid()}")

print("\n[+] PATCH COMPLETE")
print("[*] To use: import this module before running the app's main loop")
