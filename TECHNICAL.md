# 6hzs3.17 - 瀹屾暣閫嗗悜宸ョ▼鎶€鏈姤鍛?
## 1. 鎶€鏈瑕?
- **鏂囦欢**: `6hzs3.17.exe` (78.9 MB)
- **鎵撳寘宸ュ叿**: PyInstaller (2.1+) 
- **Python鐗堟湰**: 3.14.3
- **GUI妗嗘灦**: PyQt5
- **浠ｇ爜鍔犲浐**: PyArmor 9.2.3 Pro (BCC妯″紡)
- **鏋舵瀯**: PyQt5 GUI + Flask Web鏈嶅姟鍣?(绔彛5001)

## 2. 搴旂敤鏋舵瀯

### 2.1 妯″潡渚濊禆娴佺▼鍥?
```
main_pyqt_v3 (鍏ュ彛)
鈹溾攢鈹€ automation.pyc       # 娓告垙鑷姩鍖栧紩鎿?鈹?  鈹溾攢鈹€ cv2              # OpenCV 鍥惧儚璇嗗埆
鈹?  鈹溾攢鈹€ numpy            # 鐭╅樀杩愮畻
鈹?  鈹溾攢鈹€ pyautogui        # 榧犳爣閿洏妯℃嫙
鈹?  鈹溾攢鈹€ keyboard         # 閿洏鐩戝惉
鈹?  鈹斺攢鈹€ PIL (Pillow)     # 鍥惧儚澶勭悊
鈹?鈹溾攢鈹€ security.pyc         # 瀹夊叏/璁稿彲璇佹ā鍧?鈽呮牳蹇冧繚鎶?鈹?  鈹溾攢鈹€ _wmi.pyd         # WMI鏌ヨ(纭欢淇℃伅)
鈹?  鈹溾攢鈹€ 鏃堕棿楠岃瘉
鈹?  鈹?  鈹溾攢鈹€ init_time_check()     # 璇诲彇 .timestamp 鏂囦欢
鈹?  鈹?  鈹溾攢鈹€ verify_time()          # 绯荤粺鏃堕棿鍥炴嫧妫€娴?鈹?  鈹?  鈹斺攢鈹€ _get_network_time()   # NTP缃戠粶鏃堕棿鍚屾
鈹?  鈹溾攢鈹€ 蹇冭烦/Shadow绯荤粺
鈹?  鈹?  鈹溾攢鈹€ _hb_shadow_compute()  # 纭欢褰卞瓙璁＄畻
鈹?  鈹?  鈹溾攢鈹€ is_heartbeat_valid()  # 蹇冭烦楠岃瘉
鈹?  鈹?  鈹斺攢鈹€ _heartbeat_worker()   # 蹇冭烦鍙戦€佺嚎绋?鈹?  鈹溾攢鈹€ 鍙嶈皟璇曟娴?鈹?  鈹?  鈹溾攢鈹€ _check_vm_environment()      # VM妫€娴?7涓繘绋?
鈹?  鈹?  鈹溾攢鈹€ _is_debugger_present()        # 璋冭瘯鍣ㄦ娴?鈹?  鈹?  鈹溾攢鈹€ _check_suspicious_processes() # 鍙枒杩涚▼(39涓?
鈹?  鈹?  鈹溾攢鈹€ _check_loaded_dlls()          # 娉ㄥ叆DLL妫€娴?33涓?
鈹?  鈹?  鈹溾攢鈹€ _check_ce_driver()            # CE椹卞姩妫€娴?鈹?  鈹?  鈹溾攢鈹€ _check_ce_window()            # CE绐楀彛妫€娴?鈹?  鈹?  鈹斺攢鈹€ _check_dll_exports()          # DLL瀵煎嚭琛ㄦ娴?鈹?  鈹斺攢鈹€ 鍔犲瘑瀵嗛挜
鈹?      鈹溾攢鈹€ _K1 = b'6hzs'
鈹?      鈹溾攢鈹€ _K2 = b'_2024'  
鈹?      鈹溾攢鈹€ _K3 = b'_sec'
鈹?      鈹溾攢鈹€ _TS_HMAC_KEY (32瀛楄妭鏃堕棿鎴崇鍚嶅瘑閽?
鈹?      鈹溾攢鈹€ _ENC_PARTS (25涓姞瀵嗙墖娈?
鈹?      鈹斺攢鈹€ _hb_shadow_salt = 2478258319935
鈹?鈹溾攢鈹€ sso_auth.pyc         # SSO璁惧鎺堟潈 (RFC 8628)
鈹?  鈹溾攢鈹€ DPAPI鍔犲瘑 (_dpapi_encrypt/_dpapi_decrypt)
鈹?  鈹斺攢鈹€ 璁惧鐮佺櫥褰曟祦绋?鈹?鈹溾攢鈹€ activation.pyc       # 鏈湴婵€娲婚獙璇?鈹?  鈹溾攢鈹€ _HMAC_SECRET = b'6hzs_local_hmac_2024_secret_key'
鈹?  鈹溾攢鈹€ _generate_local_hmac()
鈹?  鈹斺攢鈹€ _verify_local_hmac()
鈹?鈹溾攢鈹€ cloud_config.pyc     # 浜戠閰嶇疆绠＄悊
鈹?  鈹溾攢鈹€ _V2_FIELD_REV (93涓瓧娈垫槧灏?
鈹?  鈹溾攢鈹€ _V2_TYPE_REV (37涓被鍨嬫槧灏?
鈹?  鈹斺攢鈹€ 鍥剧墖/宸ヤ綔娴佷笅杞戒笌缂撳瓨
鈹?鈹溾攢鈹€ web_server.pyc       # Flask Web绠＄悊鍚庡彴
鈹?  鈹斺攢鈹€ http://127.0.0.1:5001
鈹?鈹斺攢鈹€ editor/              # Web缂栬緫鍣ㄥ墠绔祫婧?```

### 2.2 鍚姩娴佺▼

```
1. pyarmor_runtime_011372 鍒濆鍖?   鈹斺攢鈹€ pyarmor_runtime.pyd 鍔犺浇 (C鎵╁睍, Native浠ｇ爜)

2. 妯″潡瀵煎叆闃舵
   鈹溾攢鈹€ sso_auth 瀵煎叆 鈫?璁惧鎺堟潈鍒濆鍖?   鈹溾攢鈹€ security 瀵煎叆 鈫?瀹夊叏妯″潡鍒濆鍖?   鈹?  鈹溾攢鈹€ init_time_check()       # 璇诲彇 .timestamp
   鈹?  鈹溾攢鈹€ init_integrity_check()  # 鏍￠獙鏂囦欢瀹屾暣鎬?   鈹?  鈹斺攢鈹€ _hb_shadow_compute()    # 璁＄畻纭欢鎸囩汗
   鈹溾攢鈹€ cloud_config 瀵煎叆 鈫?浜戦厤缃姞杞?   鈹溾攢鈹€ activation 瀵煎叆 鈫?鏈湴婵€娲婚獙璇?   鈹斺攢鈹€ automation 瀵煎叆 鈫?OpenCV/numpy 鍒濆鍖?
3. main_pyqt_v3.main() 鎵ц
   鈹溾攢鈹€ init_security()            # 瀹夊叏妫€鏌ュ叆鍙?   鈹?  鈹溾攢鈹€ perform_full_security_check()
   鈹?  鈹?  鈹溾攢鈹€ verify_time()       鈫?妫€鏌ユ椂闂存埑
   鈹?  鈹?  鈹溾攢鈹€ verify_integrity()  鈫?妫€鏌ユ枃浠跺畬鏁存€?   鈹?  鈹?  鈹溾攢鈹€ check VM/璋冭瘯鍣?鍙枒杩涚▼
   鈹?  鈹?  鈹斺攢鈹€ verify_hb_integrity() 鈫?妫€鏌ュ績璺?   鈹?  鈹斺攢鈹€ start_heartbeat()       # 鍚姩蹇冭烦绾跨▼
   鈹?   鈹溾攢鈹€ 鍒涘缓 QApplication
   鈹溾攢鈹€ 鍒涘缓 MainWindow / MiniWindow
   鈹溾攢鈹€ 鍚姩 WebServer (Flask, :5001)
   鈹斺攢鈹€ app.exec_() 鈫?Qt浜嬩欢寰幆
```

## 3. 璁稿彲璇侀獙璇佷綋绯昏瑙?
### 3.1 涓夊眰楠岃瘉鏋舵瀯

```
鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?绗竴灞? 鏃堕棿楠岃瘉                             鈹?鈹?.timestamp 鏂囦欢 + NTP缃戠粶鏃堕棿               鈹?鈹?妫€娴嬬郴缁熸椂闂村洖鎷?120绉掑蹇?                  鈹?鈹?缃戠粶鏃堕棿宸紓妫€娴?300绉掑蹇?                  鈹?鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?           鈹?           鈻?鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?绗簩灞? 鏈哄櫒缁戝畾 (Shadow/Heartbeat)          鈹?鈹?_hb_shadow = 纭欢鎸囩汗鍝堝笇                     鈹?鈹?_machine_id = (纭欢搴忓垪鍙?                    鈹?鈹?.machine_id 鏂囦欢                             鈹?鈹?浜戠蹇冭烦楠岃瘉 + 鏈湴HMAC楠岃瘉                   鈹?鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?           鈹?           鈻?鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?鈹?绗笁灞? 鍙嶇鏀规娴?                           鈹?鈹?鏂囦欢瀹屾暣鎬ф牎楠?                               鈹?鈹?鍙嶈皟璇?鍙峍M/鍙嶆敞鍏?                           鈹?鈹?EXE鍝堝笇鏍￠獙                                   鈹?鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?```

### 3.2 鍏抽敭鏂囦欢

| 鏂囦欢 | 鐢ㄩ€?| 浣嶇疆 |
|------|------|------|
| `.timestamp` | 鏃堕棿鎴?+ 绛惧悕 | 杞欢鏍圭洰褰?|
| `.machine_id` | 鏈哄櫒鏍囪瘑 | 杞欢鏍圭洰褰?|
| `.sso_session.bin` | SSO鐧诲綍浼氳瘽 | 杞欢鏍圭洰褰?|
| `.cloud_configs_cache.json` | 浜戦厤缃紦瀛?| 杞欢鏍圭洰褰?|
| `images/` | 涓嬭浇鐨勫浘鐗囪祫婧?| 杞欢鏍圭洰褰?|
| `workflows/` | 涓嬭浇鐨勫伐浣滄祦 | 杞欢鏍圭洰褰?|

### 3.3 鍔犲瘑瀵嗛挜浣撶郴

```
API瀵嗛挜 = _K1 + _K2 + _K3 = "6hzs_2024_sec"

鍔犲瘑瀵嗛挜v2-v8: 鐢?_ENC_PARTS (25涓墖娈? 鎷兼帴鐢熸垚
鏃堕棿鎴矵MAC瀵嗛挜: 32瀛楄妭 (_TS_HMAC_KEY)
蹇冭烦褰卞瓙: _hb_shadow = 7924664527493953526
蹇冭烦鐩愬€? _hb_shadow_salt = 2478258319935
```

## 4. PyArmor 9.2.3 Pro BCC 妯″紡鍒嗘瀽

### 4.1 BCC (Bypass Code Compile) 妯″紡

PyArmor BCC 鏄渶楂樺己搴︾殑淇濇姢妯″紡銆備唬鐮佽缂栬瘧涓猴細

```python
# 鍘熷浠ｇ爜 (琚繚鎶?:
def verify_time():
    # ... 瀹為檯閫昏緫 ...
    return (True, '鏃堕棿楠岃瘉閫氳繃')

# BCC 杞崲鍚?(瀛樺偍鍦?.pyc 涓?:
def verify_time():
    __assert_bcc__ = C_ASSERT_ARMORED_INDEX
    bcc_NNN()  # NNN = 鍔犲瘑绱㈠紩
    # 瀹為檯瀛楄妭鐮佽鍔犲瘑瀛樺偍鍦?BCC 瀵硅薄涓?```

BCC 瀵硅薄鐨勫瓧鑺傜爜鍦ㄨ繍琛屾椂鐢?`pyarmor_runtime.pyd` (Native C鎵╁睍) 鍔ㄦ€佽В瀵嗗苟鎵ц锛岃В瀵嗗悗涓嶄繚鐣欏湪鍐呭瓨涓€?
### 4.2 缁曡繃绛栫暐

鐢变簬鏃犳硶淇敼 BCC 鍔犲瘑鐨勫瓧鑺傜爜锛岄噰鐢?*鍑芥暟绾х尨瀛愯ˉ涓?(Monkey Patching)** 绛栫暐锛?
```python
# 鍦ㄦā鍧楀鍏ュ悗銆乵ain() 鎵ц鍓?鏇挎崲楠岃瘉鍑芥暟:
security.verify_time = lambda: (True, 'OK')
security.perform_security_check = lambda: (True, 'OK')
# ... 鍏?28 涓嚱鏁拌鏇挎崲
```

`main()` 鍐呴儴鐨?BCC 鍔犲瘑浠ｇ爜浠嶇劧鎵ц鍘熼€昏緫锛屼絾瀹冭皟鐢ㄧ殑瀹夊叏鍑芥暟宸茶鏇挎崲锛屽洜姝ゆ墍鏈夐獙璇佺偣閮借繑鍥?閫氳繃"銆?
## 5. 鍙嶈皟璇曟娴嬫竻鍗?
### 5.1 鍙枒杩涚▼妫€娴?(39涓?

妫€娴嬪垪琛ㄤ腑鍖呮嫭浣嗕笉闄愪簬:
- 璋冭瘯鍣? x64dbg, OllyDbg, IDA Pro, WinDbg, dnSpy
- 鐩戞帶宸ュ叿: Process Monitor, Wireshark, Fiddler, HTTP Debugger
- 娉ㄥ叆宸ュ叿: Cheat Engine, Extreme Injector

### 5.2 鍙枒DLL妫€娴?(33涓?

妫€娴嬪凡鐭ョ殑娉ㄥ叆/鍔寔DLL, 鍖呮嫭:
- 璋冭瘯鎵╁睍: ScyllaHide, TitanHide
- 娉ㄥ叆妗嗘灦: EasyHook, Detours

### 5.3 铏氭嫙鏈烘娴?(7涓?

妫€娴媀Mware/VirtualBox鐗瑰緛杩涚▼鍜屾湇鍔°€?
## 6. 鎻愬彇鐨勮В瀵嗘暟鎹?
### 6.1 瀵嗛挜鏉愭枡

```
_K1 = 0x36687A73  (b'6hzs')
_K2 = 0x5F32303234 (b'_2024')
_K3 = 0x5F736563   (b'_sec')

_TS_HMAC_KEY = 0x88F8B7D30FEFF9F03B3F42785F6FC8EE4A837AFB30182FA2C10FFCCA4F05B653
_HMAC_SECRET = b'6hzs_local_hmac_2024_secret_key'

_ENC_PARTS = 25涓姞瀵嗗瘑閽ョ墖娈?(list)

_hb_shadow = 7924664527493953526  (0x6DFC8B3A9A1A12F6)
_hb_shadow_salt = 2478258319935   (0x240D5E3A3F)
```

### 6.2 缃戠粶绔偣

```
Flask Web绠＄悊: http://127.0.0.1:5001
SSO鎺堟潈鏈嶅姟鍣? (宓屽叆寮? RFC 8628 Device Code Flow)
浜戠閰嶇疆API:   (浠嶴SO浼氳瘽涓幏鍙?
蹇冭烦鏈嶅姟鍣?     (浠庝簯閰嶇疆涓幏鍙?
```

### 6.3 鐗堟湰淇℃伅

```
缂栬瘧鏃堕棿: 2026-05-05
PyArmor: 9.2.3 Pro
PyInstaller: 2.1+
Python: 3.14.3
Qt: 5.x
OpenCV: 鎹嗙粦鐗?NumPy: 2.4.2
Flask: 3.0.0
```

## 7. 鐮磋В楠岃瘉

```
$ python run_cracked.py
[*] Initializing cracked environment...
[*] All security functions PATCHED
[*] CRACK BYPASS ACTIVATED
[*] Starting application...
[OK] sso_auth loaded
[OK] security PATCHED
[OK] cloud_config loaded  
[OK] activation PATCHED
[*] main_pyqt_v3 loaded
[*] Application started successfully

Web缂栬緫鍣ㄧ鐞嗗湴鍧€: http://127.0.0.1:5001
 * Running on http://127.0.0.1:5001 (Press CTRL+C to quit)
```

## 8. 宸ュ叿閾?
| 宸ュ叿 | 鐢ㄩ€?|
|------|------|
| pyinstxtractor-ng | PyInstaller 瑙ｅ寘 |
| Python 3.14.3 | 杩愯鏃剁幆澧?|
| decompyle3 | 瀛楄妭鐮佸弽缂栬瘧灏濊瘯 |
| sys.settrace | BCC 瑙ｅ瘑浠ｇ爜鎹曡幏 |
| dis 妯″潡 | 瀛楄妭鐮佸弽姹囩紪 | 
| ctypes | Native DLL 鍔犺浇 |
| monkey patching | 杩愯鏃跺嚱鏁版浛鎹?|
