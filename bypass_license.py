"""
6hzs3.17 璁稿彲璇佺粫杩囪ˉ涓佹ā鍧?============================
鏇挎崲鎵€鏈夊畨鍏ㄩ獙璇佸嚱鏁颁负绌哄３瀹炵幇銆?鍏辫缁曡繃 28 涓畨鍏ㄥ嚱鏁?+ SSO 璁よ瘉妯″潡銆?"""

import subprocess
import os as os_module


def patch_all():
    """鎵ц鍏ㄩ儴缁曡繃琛ヤ竵"""
    
    import sso_auth
    import security
    import activation

    # === Security 妯″潡琛ヤ竵 ===

    # 鏃堕棿楠岃瘉
    security.verify_time = lambda: (True, 'OK')
    security.init_time_check = lambda: None
    security._get_network_time = lambda: 0.0

    # 瀹屾暣鎬ч獙璇?    security.verify_integrity = lambda: True
    security.verify_hb_integrity = lambda: True
    security.init_integrity_check = lambda: 'ok'

    # 蹇冭烦绯荤粺
    security.is_heartbeat_valid = lambda: True
    security._heartbeat_ever_succeeded = True
    security._last_heartbeat_success = True
    security._force_offline_reason = None
    security.stop_heartbeat = lambda: None
    security.start_heartbeat = lambda: None
    security._heartbeat_worker = lambda: None
    security._pinned_post_for_heartbeat = lambda: None

    # 瀹夊叏妫€鏌ュ叆鍙?    security.perform_security_check = lambda: (True, 'OK')
    security.perform_full_security_check = lambda: (True, 'OK')
    security.security_check_with_warning = lambda: True
    security.init_security = lambda: None

    # 鍙嶈皟璇?鍙峍M
    security._check_vm_environment = lambda: False
    security._is_debugger_present = lambda: False
    security._check_suspicious_processes = lambda: False
    security._check_loaded_dlls = lambda: False
    security._check_ce_driver = lambda: False
    security._check_ce_window = lambda: False
    security._check_dll_exports = lambda: False

    # EXE鍝堝笇
    security._calculate_exe_hash = lambda: '0' * 40

    # === Activation 妯″潡琛ヤ竵 ===
    activation._verify_local_hmac = lambda: True
    activation.verify_activation = lambda: True

    # === SSO 璁よ瘉琛ヤ竵 ===
    sso_auth.SSOAuth = type('SSOAuth', (), {
        '__init__': lambda self, *a, **kw: None,
        'is_authenticated': lambda self: True,
        'get_access_token': lambda self: 'cracked_token',
        'refresh_token': lambda self: True,
        'logout': lambda self: None,
    })

    # === 绯荤粺璋冪敤淇濇姢琛ヤ竵 ===
    # 闃叉 BCC 鍔犲瘑瀛楄妭鐮佸唴閮ㄧ洿鎺ヨ皟鐢ㄧ郴缁熷懡浠ゅけ璐?    _orig_check_output = subprocess.check_output
    _orig_system = os_module.system

    subprocess.check_output = lambda *a, **kw: (
        _orig_check_output(*a, **kw) if False else b'FAKE_SYSTEM_ID'
    )
    os_module.system = lambda *a, **kw: 0

    # WMI 鏌ヨ淇濇姢
    try:
        import _wmi
        _wmi.exec_query = lambda *a, **kw: []
    except ImportError:
        pass

    print("[*] All 28 security functions PATCHED", flush=True)
    print("[*] CRACK BYPASS ACTIVATED", flush=True)
