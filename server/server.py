import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv 

load_dotenv()

HOST = os.environ.get("SERVER_HOST")
PORT = int(os.environ.get("SERVER_PORT"))

class MyServer(BaseHTTPRequestHandler):
    # Responds to a GET request
    def do_GET(self):
        self.send_response(200)

        # Indicates that the response is HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Path to the HTML file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        index_path = os.path.join(script_dir, '../client/index.html')

        # Opens the html file in read mode 
        with open(index_path, 'r') as file:

            # Converts the file contents to bytes and send it as the response body
            self.wfile.write(bytes(file.read(), 'utf-8'))


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyServer)
    print(f'Server started - http://{HOST}:{PORT}')
    server.serve_forever()