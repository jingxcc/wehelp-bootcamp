from flask import Blueprint, redirect, render_template, url_for, request, session
import db
import json

member_bp = Blueprint("member_bp", __name__)
db_conn, db_cursor = db.connect_db()


@member_bp.route("/member")
def member():
    if "member_id" in session:
        messages = get_messages()
        return render_template("auth/member.html", messages=messages)

    return redirect(url_for("index"))


@member_bp.route("/createMessage", methods=["POST"])
def create_message():
    content = request.form["content"]

    sql = "INSERT INTO message (member_id, content) \
        VALUES (%s, %s)"
    val = (session["member_id"], content)
    db_cursor.execute(sql, val)
    db_conn.commit()
    print(db_cursor.rowcount, "record(s) was inserted.")

    return redirect(url_for("member_bp.member"))


@member_bp.route("/deleteMessage", methods=["POST"])
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
            db_conn.commit()
            print(db_cursor.rowcount, "record(s) was deleted.")
        else:
            print("no right to delete.")

        return redirect("/member")


@member_bp.route("/api/member", methods=["GET", "PATCH"])
def api_member():
    if request.method == "GET":
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

    if request.method == "PATCH":
        try:
            request_body = json.loads(request.data)

            sql = "UPDATE member SET name = %s \
                WHERE id = %s"
            val = (request_body["name"], session["member_id"])
            db_cursor.execute(sql, val)
            db_conn.commit()
            print(db_cursor.rowcount, "record(s) was updated.")

            session["name"] = request_body["name"]

            response_data = {"ok": True}
        except Exception:
            response_data = {"error": True}

        finally:
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
