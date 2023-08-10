from flask import Flask
from flask import redirect, render_template, url_for, request, session
import db

app = Flask("__name__")
app.secret_key = "869b72a2df6d7d64f28aa1adfea15d19e98130ea9a94726382f0bbc2e13cacdd"
db_conn, db_cursor = db.connect_db()


@app.route("/")
def index():
    return render_template("index.html")


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
        session["member_id"] = result[0][0]
        session["username"] = result[0][1]
        session["name"] = result[0][2]

        return redirect(url_for("member"))
    else:
        [session.pop(key) for key in list(session.keys())]

        error_msg = "Username or password is not correct"
        return redirect(url_for("error", message=error_msg))


@app.route("/signup", methods=["POST"])
def signup():
    db_conn, db_cursor = db.connect_db()
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    # print(type(name), type(username), type(password))

    sql = "SELECT username \
        FROM member \
        WHERE username = %s"
    val = [(username)]
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
        db.close_db(db_conn)

        return redirect(url_for("index"))


@app.route("/signout")
def signout():
    [session.pop(key) for key in list(session.keys())]
    return redirect(url_for("index"))


@app.route("/member")
def member():
    if "member_id" in session:
        messages = get_message()
        return render_template("auth/member.html", messages=messages)

    return redirect(url_for("index"))


@app.route("/error")
def error():
    msg = request.args.get("message")
    return render_template("auth/error.html", msg=msg)


@app.route("/createMessage", methods=["POST"])
def create_message():
    db_conn, db_cursor = db.connect_db()
    content = request.form["content"]

    sql = "INSERT INTO message (member_id, content) \
        VALUES (%s, %s)"
    val = (session["member_id"], content)
    db_cursor.execute(sql, val)
    db_conn.commit()
    print(db_cursor.rowcount, "record(s) was inserted.")

    db.close_db(db_conn)
    return redirect(url_for("member"))


def get_message():
    db_conn, db_cursor = db.connect_db()
    sql = "SELECT m.name, msg.content FROM \
        message AS msg \
        LEFT JOIN member AS m ON msg.member_id = m.id \
        ORDER BY msg.time DESC, msg.id DESC"
    db_cursor.execute(sql)
    result = db_cursor.fetchall()

    db.close_db(db_conn)
    return result


if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)
