from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ("Hellow OWrld from flask ist geil nochmal test"git )