from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Phyo Ei Ei Bo!"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
