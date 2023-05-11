import os

def posts():
    files = []

    for file in os.listdir(f"{os.getcwd()}/posts"):
        filename = file.split(".md")[0]
        title = filename.replace('-',' ')
        files.append(
            f'<li><a href="/posts/{filename}" class="link">{title}</a></li>'
        )

    return "".join(files)