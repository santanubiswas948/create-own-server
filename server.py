from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import subprocess
class ServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self,header='text/html'):
        self.send_response(200)
        self.send_header('Content-type', header)
        self.end_headers()

    def do_GET(self):
        rt = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'create-own-server')
#HTML pages routing----------------
        if self.path == '/abc.html' or self.path == '/':
            self.path = '/abc.html'
            filename = rt + self.path
            self._set_headers()
            with open(filename, 'rb') as fh:
                html = fh.read()
                self.wfile.write(html)
#Python pages routing---------------------------
        elif self.path == '/xyz.py':
            filename = rt + self.path
            self._set_headers()
            html =  subprocess.check_output(["python", filename], shell=True)
            self.wfile.write(html)
#PHP pages routing----------------
        elif self.path == '/test.php':
            filename = rt + self.path
            self._set_headers()
            html =  subprocess.check_output(["php",filename], shell=True)
            self.wfile.write(html)
#JPG images routing----------------
        elif self.path.endswith(".jpg"):
            self._set_headers('image/jpg')
            filename = rt + self.path
            with open(filename, 'rb') as fh:
                html = fh.read()
                self.wfile.write(html)
#NOT FOUND pages routing----------------
        else:
            self._set_headers()
            self.wfile.write("<!DOCTYPE html><html><body><div><h1>404 NOT FOUND</h1></body></html".encode())#convert into bytes

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=ServerHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Start working server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
        run()
        
    