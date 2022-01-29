import requests

header = {"Content-Type": "application/json"}


def post_file(url, file_whereabout):
    try:
        file = {'file': open(file_whereabout, 'rb')}
    except Exception as e:
        return "Неверно заданный путь до файла"
    req = requests.post(url + "files", files=file)
    print(str(req.text))


def get_file(url, file_name):
    req = requests.get(url + "files", json={"file_name": file_name})
    if req.status_code == 400 | req.status_code == 404:
        return str(req.text)
    with open("storage/" + file_name, 'w') as f:
        f.write(req.text)
    return "Файл успешно скачан"


def delete_file(url, file_name):
    req = requests.delete(url + "files", json={'file_name': file_name}, headers=header)
    return str(req.text)
