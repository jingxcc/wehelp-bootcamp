from flask import Flask
from flask import redirect, render_template, url_for, request, session
import db

app = Flask("__name__")
app.secret_key = "869b72a2df6d7d64f28aa1adfea15d19e98130ea9a94726382f0bbc2e13cacdd"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    db_conn, db_cursor = db.connect_db()
    sql = "SELECT id, username, name \
        FROM member \
        WHERE username = %s AND password = %s"
    val = (username, password)
    db_cursor.execute(sql, val)
    result = db_cursor.fetchall()

    if len(result) > 0:
        session["SIGN-IN"] = "TRUE"
        session["member_id"] = result[0][0]
        session["username"] = result[0][1]
        session["name"] = result[0][2]

        return redirect(url_for("member"))
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


if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)
