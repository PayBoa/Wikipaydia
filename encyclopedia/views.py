from django.shortcuts import render
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrycontent(request, entrytitle):

    md_content = util.get_entry(entrytitle)
    html_content = markdown.markdown(md_content)


    return render(request, "encyclopedia/entrycontent.html", {
        "content": html_content,
        "entrytitle": entrytitle
    })