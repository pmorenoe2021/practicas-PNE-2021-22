import json
import http.client

server = 'rest.ensembl.org'
endpoint = '/info/ping'
params = '?content-type=application/json'
url = server + endpoint + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

conn = http.client.HTTPConnection(server)

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()