import socket
import termcolor
import os  # operative system
from Seq1 import Seq

IP = "localhost"
PORT = 8080
genes = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("The server is configured!")

    while True:
        print("Waiting for Clients ....")
        (client_socket, client_ip_port) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")

        slices = request.split(" ")
        command = slices[0]
        termcolor.cprint(f"{command}", "green")

        if command == "PING":  # 1  echo "PING"| ./nc 127.0.0.1 8080
            response = f"OK!\n"

        elif command == "GET":
            sequence_number = int(slices[1])
            sequence = genes[sequence_number]
            seq = Seq()
            filename = os.path.join("..", "..", "Genes", f"{sequence}.txt")
            seq.read_fasta(filename)
            response = f"{seq}\n"
            print(response)

        elif command == "INFO":
            bases = slices[1]
            sequence = Seq(bases)
            response = f"{sequence.info()}"

        elif command == "COMP":
            bases = slices[1]
            sequence = Seq(bases)
            response = f" {sequence.seq_complement()}\n"

        elif command == "REV":
            bases = slices[1]
            sequence = Seq(bases)
            response = f" {sequence.seq_reverse()}\n"

        elif command == "GENE":
            bases = slices[1]
            sequence = Seq()
            filename = os.path.join("..","..", "Genes", f"{bases}.txt")
            sequence.read_fasta(filename)
            response = f" {sequence}\n"

        print(response)
        response_bytes = str.encode(response)
        client_socket.send(response_bytes)

        client_socket.close()
except socket.error:
    print(f"Problems using {PORT}. Do you have permision?")

except KeyboardInterrupt:
    print("Server stopped by admin")
    server_socket.close
