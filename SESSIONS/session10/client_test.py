from Client0 import Client
IP = "localhost"
PORT = 8000
MESSAGES = 5

c = Client(IP, PORT)
for i in range(MESSAGES):
    c.debug_talk(f"Message {i}")