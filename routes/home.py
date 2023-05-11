from config import app
import os
from utils import posts

@app.get("/")
def home():
    css_file = os.getcwd() + "/static/css/index.css"
    css_link = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"

    start_html = open(os.getcwd() + "/utils/layouts/start.html","rt")
    end_html = open(os.getcwd() + "/utils/layouts/end.html","rt")
 
    posts_link = posts()

    favicon =  "https://raw.githubusercontent.com/triistam/website/main/static/favicon.ico"

    body = f"""
  <div class="container">
  <h1>Posts so far!</h1>
    {posts_link}
  </div>"""

    return start_html.read().format(css_file) + body + end_html.read()