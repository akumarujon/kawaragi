from config import app
import os

@app.get("/")
def home():
    css_file = os.getcwd() + "/static/css/index.css"
    
    start_html = open(os.getcwd() + "/utils/layouts/start.html","rt")
    end_html = open(os.getcwd() + "/utils/layouts/end.html","rt")
 
    posts_link = ""

    ext = ".md"

    for path in os.listdir(os.getcwd() + "/posts/"):
        posts_link += f"<a href='/posts/{path.split(ext)[0]}'>{path.split(ext)[0]}<a>\n"

    return start_html.read().format(css_file) + f"<ul>{posts_link}<ul>" + end_html.read()