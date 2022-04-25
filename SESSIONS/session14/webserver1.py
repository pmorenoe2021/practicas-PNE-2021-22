import http.server # para trabajar con un servidor de http
import socketserver # para trabajar con un socket del servidor (canal comunicacion)

# "" es como local host *
PORT = 8080  #Server's port

socketserver.TCPServer.allow_reuse_address = True  #for preventing the error: "Port already in use"
Handler = http.server.SimpleHTTPRequestHandler  # -- captura peticiones http y responde en consecuencia

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd: #TCPServer: para que no haya perdidas de datos durante comunicacion
    print("Serving at PORT", PORT) # httpd / d = daemon --> web_server

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()  # web_server.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()  #web_server.close()