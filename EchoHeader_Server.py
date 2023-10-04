import os
import requests
# import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_response(b'')
        # logging.error(self.headers)
    
    def do_POST(self):
        content_length = int(self.headers.get('content-legth',0))
        body = self.rfile.read(content_length)
        
        self.write_response(body)
        
    def write_response(self, content):
        
        # First, send a 200 OK response.
        self.send_response(200)
        
        
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        for h in self.headers:
            self.send_header(h, self.headers[h])
        self.end_headers()
       
        self.wfile.write(content)
        
        # Say Hello
        self.wfile.write("Hello, HTTP!\n".encode())
        
        print(self.headers)
            
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, MyRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    print("Server stopped")
           