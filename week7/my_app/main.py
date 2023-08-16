from flask import Flask, redirect, render_template, url_for, request, session
import db
from member import member_bp

app = Flask("__name__")
app.secret_key = "869b72a2df6d7d64f28aa1adfea15d19e98130ea9a94726382f0bbc2e13cacdd"
app.register_blueprint(member_bp)

db_conn, db_cursor = db.connect_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/error")
def error():
    msg = request.args.get("message")
    return render_template("auth/error.html", msg=msg)


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT id, username, name \
        FROM member \
        WHERE username = %s AND password = %s"
    val = (username, password)
    db_cursor.execute(sql, val)
    result = db_cursor.fetchall()

    if len(result) > 0:
        result = result[0]
        session["member_id"] = result["id"]
        session["username"] = result["username"]
        session["name"] = result["name"]

        return redirect(url_for("member_bp.member"))
    else:
        session.clear()

        error_msg = "Username or password is not correct"
        return redirect(url_for("error", message=error_msg))


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT username \
        FROM member \
        WHERE username = %s"
    val = (username,)
    db_cursor.execute(sql, val)
    result = db_cursor.fetchall()

    if len(result) > 0:
        error_msg = "The username has already been registered"
        return redirect(url_for("error", message=error_msg))
    else:
        sql = "INSERT INTO member (name, username, password) \
            VALUES (%s, %s, %s)"
        val = (name, username, password)

        db_cursor.execute(sql, val)
        db_conn.commit()
        print(db_cursor.rowcount, "record(s) was inserted.")

        return redirect(url_for("index"))


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)
