import http.client
from http import HTTPStatus
import json
import termcolor

SERVER = "rest.ensembl.org"
PORT = 80

GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

GENE = 'MIR633'
RESOURCE = f"/sequence/id/{GENES[GENE]}?content-type=application/json"

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", RESOURCE)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(response)
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{RESOURCE}")

if response.status == HTTPStatus.OK:
    print(f"Response received: {response.status} {response.reason}")
    print()

    raw_data = response.read().decode("utf-8")
    data = json.loads(raw_data)
    print(f"Gene: {GENE}")
    print(f"Description: {data['desc']}")
    print(f"Bases: {data['seq']}")
