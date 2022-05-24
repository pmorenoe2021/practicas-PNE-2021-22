from sequence import Seq
from http import HTTPStatus
import jinja2
import http.client
import json
from pathlib import Path

def read_template_html_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content


SERVER = 'rest.ensembl.org'
OK = 200
ERROR = 400 # SI HAY ALGUN ERROR EL ESTATUS SERA ESTE


def list_species(limit=None): # el parametro es opcional x lo que dejamos None x defecto
    endpoint = '/info/species'
    params = '?content-type=application/json'  #almacena los parametros de la peticion(guarda el cntenido en forma json)
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER) #se conecta con el ensembl
    conn.request("GET", url) # especifica el tipo de peticion
    response = conn.getresponse()
    status = OK
    if response.status == HTTPStatus.OK:
        raw_json = response.read()  #json_bytes
        str_json = raw_json.decode("utf-8")
        data = json.loads(str_json)  # nos transforma la info en string de json a un diccionario en python
        #print(data)
        try:
            species = data['species']

            context = {
                "total": len(species),
                "species": species,
                "limit": limit}
            contents = read_template_html_file("./html/species.html").render(context=context)
        except KeyError:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def karyotype(specie):
    endpoint = '/info/assembly/'
    params = f'{specie}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        #print(data)
        try:
            karyotype = data['karyotype']

            context = {
                "karyotype": karyotype,
            }
            contents = read_template_html_file("./html/karyotype.html").render(context=context)
        except KeyError:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def chromosome_length(specie, chromo):
    endpoint = '/info/assembly/'
    params = f'{specie}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        try:
            top_level_region = data['top_level_region']
            length = 0
            for chromosome in top_level_region:
                if chromosome['name'] == chromo:
                    length = chromosome['length']
                    break

            context = {
                "length": length,
            }
            contents = read_template_html_file("./html/chromosome_length.html").render(context=context)
        except KeyError:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def get_id(gene):
    endpoint = '/homology/symbol/human/'
    params = f'{gene}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    ok = True
    id = None
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        try:
            id = data['data'][0]['id']
        except (KeyError, IndexError):
            ok = False
    else:
        ok = False
    return ok, id


def gene_seq(gene):
    ok, id = get_id(gene)
    if ok:
        endpoint = '/sequence/id/'
        params = f'{id}?content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']

                context = {
                    "gene": gene,
                    "bases": bases
                }
                contents = read_template_html_file("./html/gene_seq.html").render(context=context)
            except KeyError:
                status = ERROR
                contents = Path("./html/error.html").read_text()
        else:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status =ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_info(gene):
    ok, id = get_id(gene)
    if ok:
        endpoint = '/overlap/id/'
        params = f'{id}?feature=gene;content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            print(data)
            try:
                start = data[0]['start']  # esto es una lista x eso ponemos primro la posicion
                end = data[0]['end']
                length = end - start
                chromosome_name = data[0]['assembly_name']

                context = {
                    "gene": gene,
                    "start": start,
                    "end": end,
                    "id": id,
                    "length": length,
                    "chromosome_name": chromosome_name
                }
                contents = read_template_html_file("./html/gene_info.html").render(context=context)
            except (KeyError, IndexError):
                status = ERROR
                contents = Path("./html/error.html").read_text()
        else:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_calc(gene):
    ok, id = get_id(gene)
    if ok:
        endpoint = '/sequence/id/'
        params = f'{id}?content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']
                seq = Seq(bases)
                context = {
                    "gene": gene,
                    "seq": seq
                }
                contents = read_template_html_file("./html/gene_calc.html").render(context=context)
            except KeyError:
                status = ERROR
                contents = Path("./html/error.html").read_text()
        else:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_list(chromo, start, end):
    endpoint = '/overlap/region/human/'
    params = f'{chromo}:{start}-{end}?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        print(data)
        try:
            context = {
                "data": data,
            }
            contents = read_template_html_file("./html/gene_list.html").render(context=context)
        except KeyError:
            status = ERROR
            contents = Path("./html/error.html").read_text()
    else:
        status = ERROR
        contents = Path("./html/error.html").read_text()

    return status, contents

