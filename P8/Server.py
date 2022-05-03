import os
import json
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import urlparse, parse_qs

html = "./html/"
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)  # path = url
        path = parsed_url.path
        params = parse_qs(parsed_url.query)
        print(path, params)

        if path == "/":
            context = {'n_sequences': len(SEQUENCES), 'genes': GENES}
            contents = read_html_file("index.html").render(context=context)
            self.send_response(200)

        elif path == "/basic-01":
            contents = read_html_file(path[1:] + ".html").render()
            self.send_response(200)

        elif path == "/basic-02":
            sequence_number = int(params['sequence_number'][0])  # 2
            sequence = Seq(SEQUENCES[sequence_number])  # "ATCG"
            contents = read_html_file(path[1:] + ".html").\
                render(context={'sequence_number': sequence_number, 'sequence': sequence})
            self.send_response(200)

        elif path == "/basic-03":
            gene_name = params['gene_name'][0]
            sequence = Seq()
            file_name = os.path.join("..", "Genes", f"{gene_name}.txt")
            sequence.read_fasta(file_name)
            contents = read_html_file(path[1:] + ".html"). \
                render(context={'gene_name': gene_name, 'sequence': sequence})
            self.send_response(200)


        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)

        return


with socketserver.TCPServer((""), MyHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()

#url = urlparse(self.path
#argum = parse_qs(url.query))

#if url =="/listspecies":
#n_species = argum["numb_species]
# dict_answer = make_ensembl_requests("/info/species")
#make_ensembl_request("/sequence/id" +FRAT1, ARGUMENT + "&species=homo_sapiens")
#list_species = dict_answer["species"]
#list_species = list_species[0:n_species]
#content = read_html_file("html/list_species.html")\
#    .render(context={"species": list-species})