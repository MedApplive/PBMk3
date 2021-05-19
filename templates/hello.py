from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Index Page</h1>"


@app.route("/")
def hello_world():
    return "<h1> Hello World!</h1>"


app.run(debug=True)
