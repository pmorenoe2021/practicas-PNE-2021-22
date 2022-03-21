from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7
GENE = "FRAT1"
FRAGMENTS = 10
BASES = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT1 = 8000
PORT2 = 8081

c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP, PORT2)
print(c2)

s = Seq()
s.read_fasta(f"{GENE}")
print(f"GENE {GENE}: {s}")

response1 = c1.talk(f"Sending gene {GENE} to server in fragments of 10 ")
response2 = c2.talk(f"Sending gene {GENE} to server in fragments of 10 ")

start_index = 0
end_index = BASES
for i in range(1, FRAGMENTS + 1):
    fragment = s.strbases[start_index: end_index]
    print(f"Fragment {i}: {fragment}")
    if i % 2 == 0: #server 2
        c2.talk(f"Fragment {i}: {fragment}")
    else: #server1
        c1.talk(fragment)
    start_index += BASES
    end_index += BASES
