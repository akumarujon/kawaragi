from config import app
from utils import html
import os

@app.get("/posts/<slug>/")
def post_get(slug):
    path = os.getcwd() + f"/posts/{slug}.md"
    
    if os.path.exists(path):
        post = open(path, "rt").read()
        return html(post)

    err_404_html = open(os.getcwd() + f"/templates/404.html", "rt").read()
    return err_404_html