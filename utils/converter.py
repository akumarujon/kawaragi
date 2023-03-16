import markdown
import os

def html(md_text):
    html_text = markdown.markdown(md_text)
    css_file = os.getcwd() + "/static/css/index.css"
    
    start_html = open(os.getcwd() + "/utils/layouts/start.html","rt")
    end_html = open(os.getcwd() + "/utils/layouts/end.html","rt")
 
    return start_html.read().format(css_file) + html_text + end_html.read()
