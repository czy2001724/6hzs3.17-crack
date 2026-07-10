"""
HTTP 抓包 v3 - 最小绕过，保留网络请求
"""

import sys, os, json, time

EXTRACTED_DIR = r'C:\Users\yan\Desktop\新建文件夹\extracted_src\6hzs3.17_copy.exe_extracted'
PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = r'C:\Python314'
APP_DIR = r'C:\Users\yan\Desktop\新建文件夹'
LOG_FILE = os.path.join(APP_DIR, 'http_traffic.jsonl')

# 清空旧日志
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

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

os.chdir(APP_DIR)

import importlib
importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')

# Patch requests 记录流量
import requests as req
_orig = req.Session.request

def _log(self, method, url, **kw):
    start = time.time()
    entry = {'time': time.strftime('%H:%M:%S'), 'method': method, 'url': url}
    
    j = kw.get('json')
    d = kw.get('data')
    if j: entry['body'] = j
    elif d:
        try: entry['body'] = d.decode('utf-8', errors='replace')[:1000]
        except: entry['body'] = str(d)[:500]
    
    try:
        resp = _orig(self, method, url, **kw)
        entry['status'] = resp.status_code
        entry['resp_headers'] = dict(resp.headers)
        entry['resp'] = resp.text[:3000]
        entry['elapsed'] = f"{time.time() - start:.3f}s"
        
        print(f"\n{'='*60}")
        print(f"[HTTP] {method} {url}")
        print(f"       Status: {resp.status_code} ({entry['elapsed']})")
        b = entry.get('body')
        if b: print(f"       Body: {json.dumps(b, ensure_ascii=False)[:300]}")
        print(f"       Response: {entry['resp'][:500]}")
        print(f"{'='*60}")
        
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        
        return resp
    except Exception as e:
        entry['error'] = str(e)
        print(f"\n[HTTP] {method} {url} -> ERROR: {e}")
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        raise

req.Session.request = _log
print("[*] HTTP logger active\n", flush=True)

# 导入模块，最小 patch（只绕过本地检测，保留网络请求）
import sso_auth, security, activation, cloud_config

# 只绕过纯本地检测，不绕过网络通信
security.verify_time = lambda: (True, 'OK')
security.verify_integrity = lambda: True
security.verify_hb_integrity = lambda: True
security.init_time_check = lambda: None
security.init_integrity_check = lambda: 'ok'
security._check_vm_environment = lambda: False
security._is_debugger_present = lambda: False
security._check_suspicious_processes = lambda: False
security._check_loaded_dlls = lambda: False
security._check_ce_driver = lambda: False
security._check_ce_window = lambda: False
security._check_dll_exports = lambda: False
security._calculate_exe_hash = lambda: '0' * 40
activation._verify_local_hmac = lambda: True

# 不绕过 is_heartbeat_valid, perform_security_check, heartbeat_worker 等
# 这些函数内部会发起真正的 HTTP 请求

# 保护 subprocess 调用（获取 C 盘序列号等）
import subprocess
subprocess.check_output = lambda *a, **kw: b'FAKE_SERIAL'

print("[*] Minimal bypass active (local checks only)\n", flush=True)

# 触发 init_security
print("[1] init_security()...", flush=True)
try:
    result = security.init_security(
        server_url='https://6hzszdh.isi.ink:49897/api',
        machine_id='eb8bbfcb994dd043:9cfe997eaa9cb644'
    )
    print(f"    -> {result}", flush=True)
except Exception as e:
    print(f"    -> Error: {e}", flush=True)
    import traceback
    traceback.print_exc()

# 触发 perform_security_check（这个会发 HTTP 请求）
print("\n[2] perform_security_check()...", flush=True)
try:
    result = security.perform_security_check()
    print(f"    -> {result}", flush=True)
except Exception as e:
    print(f"    -> Error: {e}", flush=True)

# 触发心跳
print("\n[3] start_heartbeat()...", flush=True)
try:
    security._heartbeat_ever_succeeded = True
    security._last_heartbeat_success = True
    security._force_offline_reason = None
    security.start_heartbeat(
        server_url='https://6hzszdh.isi.ink:49897/api',
        machine_id='eb8bbfcb994dd043:9cfe997eaa9cb644',
        interval=10
    )
    print(f"    -> Started, waiting 15s for heartbeat...", flush=True)
    time.sleep(15)
    security.stop_heartbeat()
except Exception as e:
    print(f"    -> Error: {e}", flush=True)

# SSO Auth
print("\n[4] SSOAuth login attempt...", flush=True)
try:
    sso = sso_auth.SSOAuth()
    if hasattr(sso, 'login'):
        sso.login()
        print(f"    -> Login attempted", flush=True)
    elif hasattr(sso, 'start_authorization'):
        sso.start_authorization()
        print(f"    -> Authorization started", flush=True)
except Exception as e:
    print(f"    -> Error: {e}", flush=True)

print(f"\n[*] Done. Traffic log: {LOG_FILE}")
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"[*] Log size: {len(content)} bytes")
    if content:
        print(content[:5000])
    else:
        print("[!] No HTTP requests captured")
