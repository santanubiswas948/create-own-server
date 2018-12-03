# Create-own-server
It is a simple server where it process static files and some properties added.
It is not for production used but can work fine for static files like html,jpg,png etc.
# Getting Started
## What is server?
> Server is a computer which stores data and serving the user request and running forever. We will create a socket and  it binds an adress(IP) and Port number.
## Implemantation
> For creating server we used HTTPServer as a server and it takes two things server adress(IP,PORT) and handler. When request comes server internally send request to handler and there are some methods in handlere which we are overriding for handleing the request.
## Server Code:
> If we call run functionn it creates instance of HTTPServer by passing server_address and handler_class. Server_address here a list of ip and port. By default IP is localhost and port=80. Here httpd is a server object and after calling httpd.serve_forever() it starting to work and waiting for request.
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
> At the time of server creation passes the serverhandler object by creation ServerHandler instanmce. ServerHandler this class we create which is a subclass of ```python http.server.BaseHTTPRequestHandler ```and when request comes based on request for handleing we are overwriting the methods of ```python http.server.BaseHTTPRequestHandler ```.
# Contributing
Your PRs and stars are always welcome.
- Add your new features or fixes.
- Build the project.
# Contributors
- Santanu Biswas
# Lincense
Liencensed under [MIT](LICENSE).
