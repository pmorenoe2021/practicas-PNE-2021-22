

def read_html_file(filename):  # filename = "get.html"
    contents = Path(html + filename).read_text()  # "./html/get.html"
    contents = j.Template(contents)
    return contents