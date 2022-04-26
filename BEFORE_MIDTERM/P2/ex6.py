
from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
GENE = "FRAT1"
FRAGMENTS = 5
BASES = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT = 8080

c = Client(IP, PORT)

s = Seq()
s.read_fasta(f"{GENE}")


print(f"GENE {GENE}: {s} ")

response = c.talk(f"Sending gene {GENE} to server in fragments of 10 ")

start_index = 0
end_index = BASES
for i in range(1, FRAGMENTS + 1):
    fragment = s.strbases[start_index: end_index]
    print(f"Fragment {i}: {fragment}")
    c.talk(f"Fragment {i}: {fragment}")
    start_index += BASES
    end_index += BASES

