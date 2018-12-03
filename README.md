# Create-own-server
It is a simple server where it process static files and some properties added.
It is not for production used but can work fine for static files like html,jpg,png etc.
# Documentation
## What is server?
> Server is a computer which stores data and serving the user request and running forever. We will create a socket and  it binds an adress(IP) and Port number.
## Implemantation
> For creating server we used ```http.server.HTTPServer``` as a server and it takes two things server adress(IP,PORT) and handler. When request comes to server internally send request to handler and there are some methods in handler which we overrides for handleing the request.
## Server Code:
> If we call ```run() ``` method it creates instance of ```http.server.HTTPServer``` by passing server_address and handler_class. Server_address here a list of ip and port. By default IP is localhost and port=80. Here ```httpd``` is a server object and after calling ```httpd.serve_forever()``` it starting to work and waiting for request.
```python
def run(server_class=HTTPServer, handler_class=ServerHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Start working server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
```
## ServerHandler
> At the time of server creation passes the serverhandler object by creation ServerHandler instanmce. ServerHandler this class we create which is a subclass of ``` http.server.BaseHTTPRequestHandler ```and when request comes based on request for handleing we are overwriting the methods of ``` http.server.BaseHTTPRequestHandler ```.
```python
class ServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self,header='text/html'):
        self.send_response(200)
        self.send_header('Content-type', header)
        self.end_headers()

    def do_GET(self):
        rt = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'create-own-server')
        if self.path == '/abc.html' or self.path == '/':
            self.path = '/abc.html'
            filename = rt + self.path
            self._set_headers()
            with open(filename, 'rb') as fh:
                html = fh.read()
                self.wfile.write(html)
        elif self.path.endswith(".jpg"):
            self._set_headers('image/jpg')
            filename = rt + self.path
            with open(filename, 'rb') as fh:
                html = fh.read()
                self.wfile.write(html)
        else:
            self._set_headers()
            self.wfile.write("<!DOCTYPE html><html><body><div><h1>404 NOT FOUND</h1></body></html".encode())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST Section</h1></body></html>")
```
# Contributing
Your PRs and stars are always welcome.
- Add your new features or fixes.
- Build the project.
# Contributors
- Santanu Biswas
# Lincense
Liencensed under [MIT](LICENSE).
