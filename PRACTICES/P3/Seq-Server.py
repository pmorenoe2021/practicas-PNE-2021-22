import socket
import termcolor

PORT = 8080
IP = "localhost"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("The server is configured!")

    while True:

        print("Waiting for Clients to connect")
        (client_socket, client_ip_port) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")

        slices = request.split(" ")
        command = slices[0]

        if command == "PING": #1
            termcolor.cprint("PIN command!", "green")

            response = f"OK!\n"
            print(response)
            response_bytes = str.encode(response)
            client_socket.send(response_bytes)

        elif command == "GET":
            pass #sequence_number = int(slices[1])



        client_socket.close()
except socket.error:
    print(f"Problems using {PORT}. Do you have permision?")

except KeyboardInterrupt:
    print("Server stopped by admin")
    server_socket.close









    def get(self, n):
        list_sequences = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
        while 0 < self.n < 4:
            return list_sequences[n]  # aqui te devuelve el nombre de el elemento no la sequencia entera

    def n_bases(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for e in gene:
            for base, numb in bases.items():
                if e == bases[base]:
                    numb += 1
        return bases

    #def get_percentages(self, seq):####
     #   bases = Seq.n_bases(seq):
      #  per = (bases[0] / len(seq)) * 100
       # return per

    def info(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        sequence = gene[1:]
        total_length = len(sequence)
        numb_bases = self.n_bases(sequence)
        #percentages = pass

        return sequence, total_length, numb_bases

    def complement(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        sequence = gene[1:]
        comp_list = {"A" : "T", "T" :"A", "C":"G" , "G":"C"}
        result = ""
        for base in sequence:
            for k,v in comp_list.items():
                if base == comp_list[v]:
                    result += comp_list[k]
        return result

    def reverse(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        sequence = gene[1:]
        return sequence[::-1]

    def gene(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        gene = f[f.find("\n"):].replace("\n", "")
        return gene[1:]







