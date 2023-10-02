import os
import socket
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # Add hello otherwise no content to show
        self.wfile.write("Hello, HTTP!\n".encode())
        
        # Read and print all request headers
        for line in self.rfile:
            print(line, end='')
            
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()
           