"""
6hzs3.17 许可证绕过补丁模块
============================
替换所有安全验证函数为空壳实现。
共计绕过 28 个安全函数 + SSO 认证模块。
"""

import subprocess
import os as os_module


def patch_all():
    """执行全部绕过补丁"""
    
    import sso_auth
    import security
    import activation

    # === Security 模块补丁 ===

    # 时间验证
    security.verify_time = lambda: (True, 'OK')
    security.init_time_check = lambda: None
    security._get_network_time = lambda: 0.0

    # 完整性验证
    security.verify_integrity = lambda: True
    security.verify_hb_integrity = lambda: True
    security.init_integrity_check = lambda: 'ok'

    # 心跳系统
    security.is_heartbeat_valid = lambda: True
    security._heartbeat_ever_succeeded = True
    security._last_heartbeat_success = True
    security._force_offline_reason = None
    security.stop_heartbeat = lambda: None
    security.start_heartbeat = lambda: None
    security._heartbeat_worker = lambda: None
    security._pinned_post_for_heartbeat = lambda: None

    # 安全检查入口
    security.perform_security_check = lambda: (True, 'OK')
    security.perform_full_security_check = lambda: (True, 'OK')
    security.security_check_with_warning = lambda: True
    security.init_security = lambda: None

    # 反调试/反VM
    security._check_vm_environment = lambda: False
    security._is_debugger_present = lambda: False
    security._check_suspicious_processes = lambda: False
    security._check_loaded_dlls = lambda: False
    security._check_ce_driver = lambda: False
    security._check_ce_window = lambda: False
    security._check_dll_exports = lambda: False

    # EXE哈希
    security._calculate_exe_hash = lambda: '0' * 40

    # === Activation 模块补丁 ===
    activation._verify_local_hmac = lambda: True
    activation.verify_activation = lambda: True

    # === SSO 认证补丁 ===
    sso_auth.SSOAuth = type('SSOAuth', (), {
        '__init__': lambda self, *a, **kw: None,
        'is_authenticated': lambda self: True,
        'get_access_token': lambda self: 'cracked_token',
        'refresh_token': lambda self: True,
        'logout': lambda self: None,
    })

    # === 系统调用保护补丁 ===
    # 防止 BCC 加密字节码内部直接调用系统命令失败
    _orig_check_output = subprocess.check_output
    _orig_system = os_module.system

    subprocess.check_output = lambda *a, **kw: (
        _orig_check_output(*a, **kw) if False else b'FAKE_SYSTEM_ID'
    )
    os_module.system = lambda *a, **kw: 0

    # WMI 查询保护
    try:
        import _wmi
        _wmi.exec_query = lambda *a, **kw: []
    except ImportError:
        pass

    print("[*] All 28 security functions PATCHED", flush=True)
    print("[*] CRACK BYPASS ACTIVATED", flush=True)
