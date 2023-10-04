import os
import socket
import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # Say Hello
        self.wfile.write("Hello, HTTP!\n".encode())
        
        # Read and print all request headers
        self.wfile.write(self.headers)
            
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
           