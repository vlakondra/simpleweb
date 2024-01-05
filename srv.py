import io
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from urllib.parse import urlparse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET` 
    def do_GET(self):
        print('do_GET',self.path)
        query = urlparse(self.path).query
        print("query ",query)

        self.send_response(200)
        self.send_header('Content-type','text/html; charset=UTF-8')
        self.end_headers()

        with open('index.html', 'rb') as file: 
            self.wfile.write(file.read()) # Read the file and send the contents


        # b = io.BytesIO(bytes("мир",'utf-8'))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes('Привет, мир!','utf-8'))
        # self.wfile.write(bytes("</body>", "utf-8"))
        
    # определяем метод `do_POST` 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()