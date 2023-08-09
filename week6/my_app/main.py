from flask import Flask
from flask import redirect, render_template, url_for, request, session


app = Flask("__name__")
app.secret_key = "869b72a2df6d7d64f28aa1adfea15d19e98130ea9a94726382f0bbc2e13cacdd"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    if username == "test" and password == "test":
        session["SIGN-IN"] = "TRUE"
        return redirect(url_for("member"))
    elif (not username) or (not password):
        error_msg = "Please enter username and password"
        return redirect(url_for("error", message=error_msg))
    else:
        error_msg = "Username or password is not correct"
        return redirect(url_for("error", message=error_msg))


@app.route("/signout")
def signout():
    session["SIGN-IN"] = "FALSE"
    return redirect(url_for("index"))


@app.route("/member")
def member():
    if session["SIGN-IN"] == "TRUE":
        return render_template("auth/member.html")

    return redirect(url_for("index"))


@app.route("/error")
def error():
    msg = request.args.get("message")
    return render_template("auth/error.html", msg=msg)


@app.route("/square")
@app.route("/square/<int:positive_int>")
def square(positive_int):
    if positive_int:
        result = int(positive_int) ** 2
        return render_template("calculation/square.html", result=result)
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
    app.debug = True
