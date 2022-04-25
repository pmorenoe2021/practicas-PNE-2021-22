import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

def process_client(client_socket): # -- Receive the request message
    request_bytes = client_socket.recv(2048)
    req = request_bytes.decode()

    print("Message FROM CLIENT: ")
    termcolor.cprint(req, "green")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #create several servers running on the smae port

server_socket.bind((IP, PORT)) # -- Setup up the socket's IP and PORT
server_socket.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
try:
    while True:
        print("Waiting for clients....")
        (client_socket, client_ip_port) = server_socket.accept()
        process_client(client_socket) # Service the client
        client_socket.close() # -- Close the socket

except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()

