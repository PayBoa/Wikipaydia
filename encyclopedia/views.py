from django.shortcuts import render
from . import util
import markdown
import re
from difflib import get_close_matches


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

    entries_lower = [] # Make all entries lowercase
    for i in range(len(entries)): 
        entries_lower.append(entries[i].lower())
    
    # If there is an exact match for the query in the entries, return content
    if query in entries_lower:
        return entrycontent(request, query)
    
    # Else, check if it looks like an entry

    # SUBSTRING METHOD
    #matches = []  
    #for s in entries:  # Iterate over each string in the list
    #    if query in s:  # Check if `input_string` is a substring of `s`
    #        matches.append(s)  # If True, add `s` to the matches list
    
    # REGEX METHOD
    #matches = []  
    #pattern = re.escape(query)  # Escape special characters in query
    #for s in entries:
    #    if re.search(pattern, s):  # Check if the pattern exists in the string
    #        matches.append(s)

    # DIFFLIB METHOD
    matches = get_close_matches(query, entries, n=10, cutoff=0.15)

    # Return search page with a list of all matches
    return render(request, "encyclopedia/searchresults.html", {
        "matches": matches
    })