from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class VulnerableHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        name = query.get("name", ["anonymous"])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = f"<html><body><h1>Hello, {name}</h1></body></html>"
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=VulnerableHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"💀 脆弱サーバー起動中... http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()