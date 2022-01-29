import requests


header = {"Content-Type": "application/json"}


def post_user(url, name, password):
    req = requests.post(url + "user", json = {'name': name, 'password': password}, headers=header)
    if req.status_code == 201:
        curr_session = req.json()['token']
    else:
        return "Ошибка " + str(req.status_code) + ": " + req.text
    return curr_session


def get_login(url, name, password):
    req = requests.get(url + "login", json = {'name': name, 'password': password}, headers=header)
    if req.status_code == 200:
        curr_session = req.json()['token']
    else:
        return "Ошибка " + str(req.status_code) + ": " + req.text
    return curr_session


def get_user(curr_session, url):
    req = requests.get(url + "user", json = {'token': curr_session}, headers=header)
    try:
        text = req.json()
        return text['name']
    except Exception as e:
        return "Ошибка " + str(req.status_code) + ": " + req.text


def post_todo(curr_session, url, text):
    req = requests.post(url + "todo", json = {'token': curr_session, 'text': text}, headers=header)
    try:
        text = req.json()
        return "Добавлена заметка: " + str(text['todo_id'])
    except Exception as e:
        return "Ошибка " + str(req.status_code) + ": " + req.text


def get_todo(curr_session, url):
    req = requests.get(url + "todo", json = {'token': curr_session}, headers=header)
    try:
        text = req.json()
        for line in text:
            return str(line['todo_id']) + ": " + line['text']
    except Exception as e:
        return "Ошибка " + str(req.status_code) + ": " + req.text


def put_todo(curr_session, url, todo_id, text):
    req = requests.put(url + "todo", json = {'token': curr_session, 'todo_id': todo_id, 'text': text}, headers=header)
    try:
        text = req.json()
        return "Изменена запись: " + str(text['todo_id'])
    except Exception as e:
        return "Ошибка " + str(req.status_code) + ": " + req.text


def delete_todo(curr_session, url, todo_id):
    req = requests.delete(url + "todo", json = {'token': curr_session, 'todo_id': todo_id}, headers=header)
    return req.text