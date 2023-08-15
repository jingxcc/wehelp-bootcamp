from flask import Flask, redirect, render_template, url_for, request, session
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
        result = result[0]
        session["member_id"] = result["id"]
        session["username"] = result["username"]
        session["name"] = result["name"]

        return redirect(url_for("member"))
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


@app.route("/member")
def member():
    if "member_id" in session:
        messages = get_messages()
        return render_template("auth/member.html", messages=messages)

    return redirect(url_for("index"))


@app.route("/error")
def error():
    msg = request.args.get("message")
    return render_template("auth/error.html", msg=msg)


@app.route("/createMessage", methods=["POST"])
def create_message():
    content = request.form["content"]

    sql = "INSERT INTO message (member_id, content) \
        VALUES (%s, %s)"
    val = (session["member_id"], content)
    db_cursor.execute(sql, val)
    db_conn.commit()
    print(db_cursor.rowcount, "record(s) was inserted.")

    return redirect(url_for("member"))


@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    request_data = request.get_json()

    if "msg_id" in request_data:
        msg_id = int(request_data["msg_id"])

        sql = "SELECT member_id FROM message \
            WHERE id = %s"
        val = (msg_id,)
        db_cursor.execute(sql, val)
        result = db_cursor.fetchall()

        if session["member_id"] == result[0]["member_id"]:
            sql = "DELETE FROM message \
                WHERE id = %s"
            val = (msg_id,)

            db_cursor.execute(sql, val)
            print(db_cursor.rowcount, "record(s) was deleted.")
            db_conn.commit()
        else:
            print("no right to delete.")

        return redirect("/member")


@app.route("/api/member")
def api_member():
    username = request.args.get("username")

    sql = "SELECT id, name, username FROM member \
        WHERE username = %s"
    val = (username,)
    db_cursor.execute(sql, val)
    result = db_cursor.fetchall()

    response_data = {"data": {}}
    if len(result) > 0:
        response_data["data"]["id"] = result[0]["id"]
        response_data["data"]["name"] = result[0]["name"]
        response_data["data"]["username"] = result[0]["username"]
    else:
        response_data["data"] = None

    return response_data


def get_messages():
    sql = "SELECT m.name, msg.content, msg.member_id, msg.id FROM \
        message AS msg \
        LEFT JOIN member AS m ON msg.member_id = m.id \
        ORDER BY msg.time DESC, msg.id DESC"
    db_cursor.execute(sql)
    messages = db_cursor.fetchall()
    # print(messages)
    return messages


if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)
