import http.server
import socketserver
import termcolor

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        contents = "Resource not available"
        if self.path == "/":
            contents = "Welcome to my server"
            self.send_response(200)
        else:
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_response(200)  # -- Status line: OK!
        self.send_header('Content-Type', 'text/plain') # Define the content-type header:
        self.send_header('Content-Length', len(contents_bytes))
        self.end_headers()
        self.wfile.write(contents_bytes)

        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
