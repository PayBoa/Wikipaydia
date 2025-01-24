from django.shortcuts import render
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entrycontent(request, entrytitle):
    md_content = util.get_entry(entrytitle)
    if md_content is None and entrytitle != "searchresults":
        return render(request, "encyclopedia/notfound.html", {
            "entrytitle": entrytitle
        })
    else:
        html_content = markdown.markdown(md_content)
        return render(request, "encyclopedia/entrycontent.html", {
            "content": html_content,
            "entrytitle": entrytitle
        })
    
def searchresults(request):
    query = request.GET.get('q', '').lower() # Get the query in lowercase
    entries = util.list_entries() # List all entries

    for i in range(len(entries)): # Make all entries lowercase
        entries[i] = entries[i].lower()

    # If there is a match for the query in the entries, return content
    if query in entries:
        return entrycontent(request, query)
    
    return render(request, "encyclopedia/searchresults.html")