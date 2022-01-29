import requests


header = {"Content-Type": "application/json"}


def post_user(url):
    curr_session = ""
    name = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    req = requests.post(url + "user", json = {'name': name, 'password': password}, headers=header)
    if req.status_code == 201:
        curr_session = req.json()['token']
    else:
        print("Ошибка " + str(req.status_code) + ": " + req.text)
    print(curr_session)
    return curr_session


def get_login(url):
    curr_session = ""
    name = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    req = requests.get(url + "login", json = {'name': name, 'password': password}, headers=header)
    if req.status_code == 200:
        curr_session = req.json()['token']
    else:
        print("Ошибка " + str(req.status_code) + ": " + req.text)
    print(curr_session)
    return curr_session


def get_user(curr_session, url):
    req = requests.get(url + "user", json = {'token': curr_session}, headers=header)
    try:
        text = req.json()
        print(text['name'])
    except Exception as e:
        print("Ошибка " + str(req.status_code) + ": " + req.text)


def post_todo(curr_session, url):
    text = input("Введите текст заметки: ")
    req = requests.post(url + "todo", json = {'token': curr_session, 'text': text}, headers=header)
    try:
        text = req.json()
        print("Добавлена заметка: " + str(text['todo_id']))
    except Exception as e:
        print("Ошибка " + str(req.status_code) + ": " + req.text)


def get_todo(curr_session, url):
    req = requests.get(url + "todo", json = {'token': curr_session}, headers=header)
    try:
        text = req.json()
        for line in text:
            print(str(line['todo_id']) + ": " + line['text'])
    except Exception as e:
        print("Ошибка " + str(req.status_code) + ": " + req.text)


def put_todo(curr_session, url):
    todo_id = input("Введите номер заметки: ")
    text = input("Введите текст заметки: ")
    req = requests.put(url + "todo", json = {'token': curr_session, 'todo_id': todo_id, 'text': text}, headers=header)
    try:
        text = req.json()
        print("Изменена запись: " + str(text['todo_id']))
    except Exception as e:
        print("Ошибка " + str(req.status_code) + ": " + req.text)


def delete_todo(curr_session, url):
    todo_id = input("Введите номер заметки: ")
    req = requests.delete(url + "todo", json = {'token': curr_session, 'todo_id': todo_id}, headers=header)
    print(req.text)