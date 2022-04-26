from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT = 8000

c = Client(IP, PORT)

seqs_l = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in seqs_l:
    s = Seq()
    s.read_fasta(f"{gene}")
    c.talk(f"Sending the {gene} Gene to the server...")
    c.talk(str(s))


