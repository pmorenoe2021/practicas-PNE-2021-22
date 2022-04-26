import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

def process_client(client_socket):  # -- Receive the request message
    req_bytes = client_socket.recv(2048)
    req = req_bytes.decode()

    print("Message FROM CLIENT: ")
    lines = req.splitlines()  # -- Split the request messages into lines
    req_line = lines[0]  # -- The request line is the first
    slices = req_line.split(" ")  # slices = ["GET", "/directory/other/file.html", "HTTP/1.0"]
    method = slices[0] # nos da el GET
    path = slices[1]
    version = slices[2]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

# RESPUESTA HTTP(necesita formato http)

    status_line = "HTTP/1.1 200 OK\n"  # We respond that everything is ok (200 code)
    body = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Green server</title>
          </head>
          <body style="background-color: lightgreen;">
            <h1>GREEN SERVER</h1>
            <p>I am the Green Server! :-)</p>
          </body>
        </html>
        """
    header = "Content-Type: text/html\n"  # Content-Type:serv indica a cliente formato dl cuerpo d respuesta
    header += f"Content-Length: 5\n"  # Content-Length: longitud contenido
    response_msg = status_line + header + "\n" + body  # -- Build the message by joining together all the parts
    response_bytes = response_msg.encode()
    client_socket.send(response_bytes)


#MAIN PROG
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # create several servers running on the smae port

    server_socket.bind((IP, PORT))  # -- Setup up the socket's IP and PORT
    server_socket.listen()

    print("SEQ Server configured!")

    try:
        while True:
            print("Waiting for clients....")
            (client_socket, client_ip_port) = server_socket.accept()
            process_client(client_socket)  # Service the client
            client_socket.close()  # -- Close the socket

    except KeyboardInterrupt:
        print("Server Stopped!")
        server_socket.close()

## sol:  no me printa nada porque lo unico que lee:
# <!DOC del body, entonces no lee ningun tipo de contenido
# SIEMPRE TENGO QUE CORRESPONDER LA LONGITUD DEL CUERPO, SI NO NOS APARECERA LA PAGINA EN BLANCO