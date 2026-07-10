"""
分析所有明文可修改的配置数据（非 BCC 加密部分）
"""

import sys, os, importlib, json

EXTRACTED_DIR = r'C:\Users\yan\Desktop\新建文件夹\extracted_src\6hzs3.17_copy.exe_extracted'
PYZ_DIR = os.path.join(EXTRACTED_DIR, 'PYZ.pyz_extracted')
PYTHON_DIR = r'C:\Python314'
APP_DIR = r'C:\Users\yan\Desktop\新建文件夹'

sys.path = [
    EXTRACTED_DIR, PYZ_DIR,
    os.path.join(PYTHON_DIR, 'Lib'),
    os.path.join(PYTHON_DIR, 'Lib', 'site-packages'),
    PYTHON_DIR,
    os.path.join(PYTHON_DIR, 'python314.zip'),
    os.path.join(PYTHON_DIR, 'DLLs'),
]
for d in [EXTRACTED_DIR, PYTHON_DIR]:
    try: os.add_dll_directory(d)
    except: pass
os.chdir(APP_DIR)

importlib.import_module('pyarmor_runtime_011372.pyarmor_runtime')
import security, activation, cloud_config, sso_auth

print("=" * 60)
print("1. CLOUD CONFIG - 明文配置数据")
print("=" * 60)

# _V2_FIELD_REV 和 _V2_TYPE_REV 是明文字典
print(f"\n_V2_TYPE_REV ({len(cloud_config._V2_TYPE_REV)} entries):")
for k, v in list(cloud_config._V2_TYPE_REV.items())[:20]:
    print(f"  {k}: {v}")

print(f"\n_V2_FIELD_REV ({len(cloud_config._V2_FIELD_REV)} entries):")
for k, v in list(cloud_config._V2_FIELD_REV.items())[:30]:
    print(f"  {k}: {v}")

print("\n" + "=" * 60)
print("2. SECURITY - 密钥材料")
print("=" * 60)
print(f"_K1: {security._K1}")
print(f"_K2: {security._K2}")
print(f"_K3: {security._K3}")
print(f"_TS_HMAC_KEY: {security._TS_HMAC_KEY.hex()}")
print(f"_hb_shadow: {security._hb_shadow}")
print(f"_hb_shadow_salt: {security._hb_shadow_salt}")
print(f"_NET_CHECK_COOLDOWN: {security._NET_CHECK_COOLDOWN}")
print(f"_ENC_PARTS: {len(security._ENC_PARTS)} items")

# Try to read _ENC_PARTS
if hasattr(security, '_ENC_PARTS'):
    print(f"  _ENC_PARTS content:")
    for i, p in enumerate(security._ENC_PARTS):
        if isinstance(p, (str, bytes)):
            print(f"    [{i}]: {p[:100] if isinstance(p, (str,bytes)) else p}")

print("\n" + "=" * 60)
print("3. ACTIVATION - 认证配置")
print("=" * 60)
print(f"_HMAC_SECRET: {activation._HMAC_SECRET}")

print("\n" + "=" * 60)
print("4. SSO AUTH - 授权端点")
print("=" * 60)
# Look for URLs in sso_auth module
for name in dir(sso_auth):
    if not name.startswith('_'):
        continue
    try:
        val = getattr(sso_auth, name)
        if isinstance(val, str) and ('http' in val or '://' in val or '.' in val):
            print(f"  {name}: {val}")
    except:
        pass

# Also check for URL-like strings in module constants
print("\n5. 配置文件内容")
print("=" * 60)

# Read .cloud_configs_cache.json
cache_file = os.path.join(APP_DIR, '.cloud_configs_cache.json')
if os.path.exists(cache_file):
    with open(cache_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n.cloud_configs_cache.json:")
    print(json.dumps(data, ensure_ascii=False, indent=2))

# Read .timestamp
ts_file = os.path.join(APP_DIR, '.timestamp')
if os.path.exists(ts_file):
    with open(ts_file, 'r') as f:
        print(f"\n.timestamp: {f.read().strip()}")

# Read .machine_id
mi_file = os.path.join(APP_DIR, '.machine_id')
if os.path.exists(mi_file):
    with open(mi_file, 'r') as f:
        print(f"\n.machine_id: {f.read().strip()}")

print("\n" + "=" * 60)
print("6. 各模块函数签名（可见逻辑入口）")
print("=" * 60)

# List all functions in each module with their signatures
for mod_name, mod in [('security', security), ('activation', activation), 
                       ('cloud_config', cloud_config), ('sso_auth', sso_auth)]:
    print(f"\n[{mod_name}]")
    for name in dir(mod):
        if name.startswith('_'):
            continue
        try:
            attr = getattr(mod, name)
            if callable(attr):
                import inspect
                try:
                    sig = inspect.signature(attr)
                    doc = inspect.getdoc(attr)
                    if doc:
                        print(f"  {name}{sig}")
                        print(f"    -> {doc.strip()}")
                    else:
                        print(f"  {name}{sig}")
                except:
                    print(f"  {name}(...)")
        except:
            pass

print("\n[DONE]")
