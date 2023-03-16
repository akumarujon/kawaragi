from config import app

@app.get("/")
def home():
    return "Hello World!"