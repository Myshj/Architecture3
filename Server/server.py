# coding=utf-8
__author__ = 'Alexey'

from UserDatabaseWork.UserDatabaseWork import UserDB
from UserDatabaseWork.User import User

from bottle import route, template, run, static_file, delete, post, put


db = UserDB("localhost", 6379, 0)


@route('/static/<filename>')
def send_static(filename):
    """
        За запитом ('/static/<filename>') відсилає статичний файл, заданий параметром filename.
        Цей файл повинен міститися у теці "static".
    """
    return static_file(filename, root='./static/')


@route('/')
def index():
    """
        За запитом ('/') повертає головну сторінку, що визначена у файлі "main.html".
    """
    file = open("html/main.html")
    temp = file.read()
    file.close()

    user_list = db.read_all_users()

    return template(temp, users=user_list)


@delete("/users/<user_id>")
def delete_user(user_id):
    db.delete_user_by_id(int(user_id))


@delete("/users/<user_id>/<email>")
def delete_email_from_user(user_id, email):
    db.delete_email_by_user_id(int(user_id), email)


@post("/users/<user_id>/<email>")
def add_email_for_user(user_id, email):
    db.create_email_for_user(int(user_id), email)

@post("/users/<user_name>/<email>")
def add_user(user_name, email):
    db.create_user(User(user_name, {email}))

@put("/users/<user_id>/<user_name>")
def update_user_name(user_id, user_name):
    db.update_user_by_id(int(user_id), User(user_name, db.read_user_by_id(int(user_id)).get_emails()))


run(host='localhost', port=8080)
