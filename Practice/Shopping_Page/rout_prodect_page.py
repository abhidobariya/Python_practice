from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my shopping website!"

@app.route("/products")
def products():
    return "Here are our products!"

@app.route("/cart")
def cart():
    return "Here is your cart!"
