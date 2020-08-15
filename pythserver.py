import http.server
from os import path
from urllib.parse import urlparse
from urllib.parse import parse_qs
from http.server import SimpleHTTPRequestHandler, HTTPServer #python 3

class HandleRequests(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        query_components = parse_qs(urlparse(self.path).query)
        if 'input' in query_components:
            data_list = query_components['input'][0].split(',')
            print(data_list[0])
            print(data_list[1])
        success = "yes"
        self.wfile.write(success.encode())
        return

    def do_PUT(self):
        self.do_POST()

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


host = 'localhost'
port = 443
HTTPServer((host, port), HandleRequests).serve_forever()

