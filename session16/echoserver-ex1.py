import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            contents = Path("form-ex1.html").read_text()
            self.send_response(200)

        elif self.path.startswith("/echo?"):
            parsed_url = urlparse(self.path)
            param = parse_qs(parsed_url.query) # la peticion, en dicionario
            try:
                msg_param = param['msg'][0]
                contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>RESULT</title>
                      </head>
                      <body>
                            <h1>Recieved message:</h1>
                            <p>{msg_param}</p>
                            <a href= "/">Main page</a>
                      </body>
                    </html>"""
            except (KeyError, IndexError):
                contents = Path("error.html").read_text()
                self.send_response(404)
        else:
            contents = Path("error.html").read_text()
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_response(200)  # -- Status line: OK!
        self.send_header('Content-Type', 'text/html') # Define the content-type header:
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