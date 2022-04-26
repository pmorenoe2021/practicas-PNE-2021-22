import socket

PORT = 8080
IP = "127.0.0.1" # or "localhost o mismo

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen() # numero inf de conexiones abiertas

print("The server is configured!")

print("Waiting for Clients to connect")
server_socket.accept()

print("A client has connected to the server!")

server_socket.close()