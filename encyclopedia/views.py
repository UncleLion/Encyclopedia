from django.shortcuts import render
from markdown import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    title_name = f"{title}"
    text_html = util.get_entry(title)
    if text_html is None:
        text_html =f"Page {title} has not been found!"
    else:
        text_html = markdown(open(f"entries/{title}.md").read())
    return render(request, "encyclopedia/title.html", {
        "title_name": title_name,
        "text_html": text_html,
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })