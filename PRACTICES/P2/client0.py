
class Client:
    def __init__(self, ip, port):
        self.ip = "127.0.0.1"
        self.port = 8080

    def ping(self):
        print("OK")

    def __str__(self):
        ip = self.ip
        port = self.port
        return (f"Connection to SERVER at {ip}, PORT: {port}")

    def talk(self, msg):
        import socket
        import termcolor
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To Server: ", end="")
        termcolor.cprint(msg, "blue")
        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")
        print("From server:")
        print()
        termcolor.cprint(response, "green")
        s.close()

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




