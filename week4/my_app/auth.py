# import sys as system
# print(system.path)


from flask import Flask
from flask import flash, redirect, render_template, url_for, request

# from flask import Blueprint
# bp = Blueprint("auth", __name__, url_prefix="/auth")

app = Flask("__name__")


# @bp.route("/register", methods=("GET", "POST"))
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin/", methods=("GET", "POST"))
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "test" and password == "test":
            return redirect(url_for("member"))
        elif (not username) or (not password):
            error_msg = "Please enter username and password"
            return redirect(url_for("error", message=error_msg))
        else:
            error_msg = "Username or password is not correct"
            return redirect(url_for("error", message=error_msg))


@app.route("/member/")
def member():
    return render_template("auth/member.html")


@app.route("/error")
def error():
    msg = request.args.get("message")
    return render_template("auth/error.html", msg=msg)
