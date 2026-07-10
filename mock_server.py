"""
本地模拟服务器 - 用内置 http.server，无需 flask
"""

import json, os, time
from http.server import HTTPServer, BaseHTTPRequestHandler

LOG_FILE = r'C:\Users\yan\Desktop\新建文件夹\server_log.jsonl'

class MockHandler(BaseHTTPRequestHandler):
    
    def log_request_to_file(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8', errors='replace') if content_len else ''
        
        entry = {
            'time': time.strftime('%H:%M:%S'),
            'method': self.command,
            'path': self.path,
            'headers': dict(self.headers),
            'body': body[:2000],
        }
        
        print(f"\n[REQ] {self.command} {self.path}")
        if body:
            print(f"      Body: {body[:300]}")
        
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)
    
    def do_POST(self):
        self.log_request_to_file()
        
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8', errors='replace')
        data = json.loads(body) if body else {}
        
        path = self.path.rstrip('/')
        
        # /api/heartbeat
        if 'heartbeat' in path:
            print(f"      -> heartbeat: machine_id={data.get('machine_id')}, password={data.get('password')}")
            self.send_json({
                "status": "ok",
                "message": "heartbeat acknowledged",
                "server_time": int(time.time()),
                "next_interval": 600
            })
        
        # /api/verify or /api/check
        elif 'verify' in path or 'check' in path:
            self.send_json({
                "status": "ok",
                "valid": True,
                "message": "verification passed"
            })
        
        # /api/activate or /api/auth
        elif 'activate' in path or 'auth' in path:
            self.send_json({
                "status": "ok",
                "token": "activated_token_here",
                "expires_at": "2099-12-31T23:59:59Z"
            })
        
        # SSO token endpoint
        elif 'token' in path or 'oauth' in path:
            self.send_json({
                "access_token": "mock_access_token",
                "token_type": "bearer",
                "expires_in": 86400,
                "refresh_token": "mock_refresh_token"
            })
        
        # Config download
        elif 'config' in path or 'cloud' in path:
            self.send_json({
                "status": "ok",
                "workflows": [],
                "images": [],
                "version": 1
            })
        
        # Unknown - log and return ok
        else:
            print(f"      [UNKNOWN] {path}")
            self.send_json({
                "status": "ok",
                "message": f"received at {path}"
            })
    
    def do_GET(self):
        self.log_request_to_file()
        path = self.path.rstrip('/')
        
        if 'device' in path or 'authorize' in path:
            self.send_json({
                "device_code": "mock_device_code",
                "user_code": "MOCK-CODE",
                "verification_uri": "http://127.0.0.1:8080/verify",
                "expires_in": 900,
                "interval": 5
            })
        else:
            self.send_json({"status": "ok", "path": path})
    
    def log_message(self, format, *args):
        pass  # 禁止默认日志

if __name__ == '__main__':
    print("=" * 60)
    print("本地模拟服务器")
    print("监听: http://127.0.0.1:8080")
    print("所有请求记录到: server_log.jsonl")
    print("=" * 60)
    
    server = HTTPServer(('127.0.0.1', 8080), MockHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        server.shutdown()
