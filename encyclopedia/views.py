from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrycontent(request, entrytitle):
    return render(request, "encyclopedia/entrycontent.html", {
        "content": util.get_entry(entrytitle),
        "entrytitle": entrytitle
    })