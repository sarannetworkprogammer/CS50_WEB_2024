from django.shortcuts import render
import markdown
from . import util



def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()

    if content == None:
        return None
    else:
        return markdowner.convert(content)





def index(request):

    entries = util.list_entries()
    css_file = util.get_entry("CSS")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

