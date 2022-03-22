
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def ping(self):
        print("OK")

    def talk(self, msg):
        import socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))
        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")
        client_socket.close()

        return response

    def debug_talk(self, msg):
        import socket
        import termcolor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))

        print("To Server: ", end="")
        termcolor.cprint(msg, "blue")
        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")
        print("From server:")
        print()
        termcolor.cprint(response, "green")
        client_socket.close()

        return response


    def valid_filename(self):
        exit = False
        while not exit:
            filename = input("NAME OF THE FILE : ")
            try:
                f = open("./Genes/" + filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                print("file does not exist")

    def get_gene(self, filename):
        f = open("./Genes/" + filename + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        return gene




