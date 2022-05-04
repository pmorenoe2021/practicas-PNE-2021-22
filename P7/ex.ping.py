import http.client
from http import HTTPStatus
import json

SERVER = "rest.ensembl.org"
PORT = 80
RESOURCE = "/info/ping?content-type=application/json"

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", RESOURCE)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()

print(response)
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{RESOURCE}")


if response.status == HTTPStatus.OK:
    print(f"Response received: {response.status}{response.reason}")
    print()

    raw_data = response.read().decode("utf-8")
    ping = json.loads(raw_data)['ping']
    if ping == 1:
        print("PING OK! The data base is running")
