# import sys as system
# print(system.path)

import functools

from flask import Flask
from flask import flash, redirect, render_template, url_for

# from flask import Blueprint
# bp = Blueprint("auth", __name__, url_prefix="/auth")

app = Flask("__name__")


# @bp.route("/register", methods=("GET", "POST"))
@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/")
# def index():
#     # return "Index Page"
#     return redirect(url_for("login"))


# @app.route("/login/")
# def login():
#     return "login"


# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello(name=None):
#     # return "<h1>Hello World !</h1>"
#     return render_template("index.html", name=name)

# from markupsafe import escape
# @app.route("/user/<name>/")
# def profile(name):
#     return f"<h1>Hello, {escape(name)}!</h1>"


# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("login"))
#     print(url_for("hello"))
#     print(url_for("hello", name="Jing"))
