from seq_client import Client

IP = "localhost"
PORT = 8081
BASES = "ACCTTGG"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

c = Client(IP, PORT)
print(c)

c.debug_talk("PING")
print()

for n in range(5):
    c.debug_talk(f"GET {n}")
    print()

c.debug_talk(f"INFO {BASES}")

print()

c.debug_talk(f"COMP {BASES}")
print()

c.debug_talk(f"REV {BASES}")

print()

for gene in GENES:
    c.debug_talk(f"GENE {gene}")
    print()

