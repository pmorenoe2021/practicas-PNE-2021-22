import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import utilities as ut
from pathlib import Path

PORT = 8080
ENDPOINTS = ["/", "/listSpecies", "/karyotype", "/chromosomeLength", "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]
# lista con las peticiones validas que puede hacer el cliente
socketserver.TCPServer.allow_reuse_address = True


def handle_karyotype(parameters):
    error = False
    contents = ""
    status = 400
    if len(parameters) == 1:
        try:
            specie = parameters['specie'][0]
            status, contents = ut.karyotype(specie)
        except (KeyError, IndexError):
            error = True
    else:
        error = True

    return status, contents, error


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        url = urlparse(self.path)
        endpoint = url.path  #(endpoint = path)
        parameters = parse_qs(url.query)
        print("Endpoint: ", endpoint)
        print("Parameters: ", parameters)

        error = False   # si hay error al acceder al servidor cambiar a true
        contents = ""  # conbtine el cuerpo de la respuesta al cliente
        status = 400
        if endpoint in ENDPOINTS:  # comprobando si la peticion es valida

            if endpoint == "/":
                status = 200
                contents = Path("./html/index.html").read_text()

            elif endpoint == "/listSpecies":
                if len(parameters) == 0:
                    status, contents = ut.list_species()
                elif len(parameters) == 1:
                    try:
                        limit = int(parameters['limit'][0])
                        status, contents = ut.list_species(limit)
                    except (KeyError, IndexError, ValueError):
                        error = True
                else:  # si me dAN mas de un parametro
                    error = True

            elif endpoint == "/karyotype": # calculado en la funcion de arriba
                status, contents, error = handle_karyotype(parameters)

            elif endpoint == "/chromosomeLength":
                if len(parameters) == 2:
                    try:
                        specie = parameters['specie'][0]
                        chromo = parameters['chromo'][0]
                        status, contents = ut.chromosome_length(specie, chromo)
                    except (KeyError, IndexError):
                        error = True
                else:
                    error = True

     #  medium level

            elif endpoint == "/geneSeq":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = ut.gene_seq(gene)
                    except (KeyError, IndexError):
                        error = True
                else:
                    error = True

            elif endpoint == "/geneInfo":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = ut.gene_info(gene)
                    except (KeyError, IndexError):
                        error = True
                else:
                    error = True

            elif endpoint == "/geneCalc":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = ut.gene_calc(gene)
                    except (KeyError, IndexError):
                        error = True
                else:
                    error = True

            elif endpoint == "/geneList":
                if len(parameters) == 3:
                    try:
                        chromo = int(parameters['chromo'][0]) # podemos ponerlo como entero o no (int).
                        start = int(parameters['start'][0])  # "
                        end = int(parameters['end'][0])  # "
                        status, contents = ut.gene_list(chromo, start, end)
                    except (KeyError, ValueError, IndexError):
                        error = True
                else:
                    error = True
        else:
            error = True

        if error:  # si no hay ningun error rellenamos con lo siguiente
            contents = Path("./html/error.html").read_text()

        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())

handler = TestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
