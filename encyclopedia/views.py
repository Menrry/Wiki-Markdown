from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
#    entries = util.list_entries()
#    css_file = util.get_entry("CSS")
#    coffee = util.get_entry("coffee")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()      # devuelve una lista de los nombres de todas las entradas de la enciclopedia guardadas actualmente.
    })
#titulo es el nombre de la variable que esperamos recibir
def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist"
        }) 
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']  # q es el nombre que le damos al input de search en layout.html
        html_content = convert_md_to_html(entry_search) # entry_search es nuestra busqueda
        if html_content is not None:                    # Si no viene vacío
            return render(request, "encyclopedia/entry.html", {  #aquí me dirige a entry.html
                "title": entry_search,   # Este es el valor que está buscando
                "content": html_content  #lo unico que convirtio a html fué el contenido del archivo *.md
            })  # search sólo va a colocar los titulos que coinciden con esas letras
        else:               # al contrario es un GET---> carga la pagina
            allEntries = util.list_entries()
            recomendation = []        # recomendación será la lista con todos los entries
            for entry in allEntries:
                if entry_search.lower() in entry.lower(): # al entry que busco lo compara en minuscula
                    recomendation.append(entry)  # carga la lista
            return render(request, "encyclopedia/search.html", {
                "recomendation": recomendation
            })
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exist"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']  # entry_title esta en entry.html---> <input type="hidden" name="entry_title" value="{{ title }}">  
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": html_content
    })