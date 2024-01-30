from django.shortcuts import redirect, render
from . import util
import markdown2
import random as rnd
from django.utils.safestring import mark_safe



def index(request):
    entries = util.list_entries()
    query = request.POST.get('q')

        

    #return redirect('/wiki/entry', title=query)
    
    #entry = util.get_entry(request.POST.get('q'))
    if request.method == 'POST':
        matched_entries = []
        for entry in entries:
            if query.lower() == entry.lower():
                return redirect(f'/wiki/{entry}', title=query)
            else:
                if query.lower() in entry.lower():
                    matched_entries.append(entry)

        return render(request, "encyclopedia/index.html", {
            "entries": matched_entries or ["No results found"]
        })
        

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):

    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/not-found.html", {
            "entry": title
        })
    
    entry = markdown2.markdown(entry)
    entry_html = mark_safe(entry) 
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry_html
    })


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        entries = util.list_entries()

        if title in entries:
            return render(request, "encyclopedia/error.html", {
                "entry": title
            })

        util.save_entry(title, content)

        return redirect(f'/wiki/{title}')

    return render(request, "encyclopedia/create.html")


def edit(request, title):
    if request.method == 'POST':
        content = request.POST.get('content')

        util.save_entry(title, content)

        return redirect(f'/wiki/{title}')

    entry = util.get_entry(title)

    return render(request, "encyclopedia/edit.html", {
        "content": entry,
        "title": title
    })

def random(request):
    entries = util.list_entries()
    entry = rnd.choice(entries)
    return redirect(f'/wiki/{entry}')

def error(request):
    title = request.POST.get('title')
    return render(request, "encyclopedia/error.html", {
        "entry": title or "Entry"
    })

