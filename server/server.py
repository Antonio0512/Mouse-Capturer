import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv 

load_dotenv()

HOST = os.environ.get("HOST")
PORT = int(os.environ.get("SERVER_PORT"))

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        index_path = os.path.join(script_dir, '../client/index.html')

        with open(index_path, 'r') as file:
            self.wfile.write(bytes(file.read(), 'utf-8'))


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyServer)
    print(f'Server started http://{HOST}:{PORT}')
    server.serve_forever()