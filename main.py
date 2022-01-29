from NotebookAPIFunctions import *
from StorageAPIFunctions import *


url = "http://dvfuflaskmachine.westus2.cloudapp.azure.com/"


def NotebookAPI():
    isAlive = True
    isAuthenticated = False
    curr_session = ""

    while isAlive:
        if not isAuthenticated:
            print("1: создать пользователя;")
            print("2: произвести вход в существующую учётную запись пользователя.")
            inp = int(input())

            if inp == 1:
                name = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")

                curr_session = post_user(url, name, password)
                print(curr_session)

                if (len(curr_session) > 0):
                    isAuthenticated = True
            elif inp == 2:
                name = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")

                curr_session = get_login(url, name, password)
                print(curr_session)

                if (len(curr_session) > 0):
                    isAuthenticated = True
            else:
                isAlive = False
        else:
            print("1: получить имя пользователя;")
            print("2: создать заметку;")
            print("3: получить список заметок;")
            print("4: изменить существующую заметку;")
            print("5: удалить существующую заметку;")
            print("6: выйти из учётной записи пользователя.")
            inp = int(input())

            if inp == 1:
                result = get_user(curr_session, url)
                print(result)
            elif inp == 2:
                text = input("Введите текст заметки: ")

                result = post_todo(curr_session, url, text)

                print(result)
            elif inp == 3:
                result = get_todo(curr_session, url)

                print(result)
            elif inp == 4:
                todo_id = input("Введите номер заметки: ")
                text = input("Введите текст заметки: ")

                result = put_todo(curr_session, url, todo_id, text)

                print(result)
            elif inp == 5:
                todo_id = input("Введите номер заметки: ")

                result = delete_todo(curr_session, url, todo_id)

                print(result)
            elif inp == 6:
                isAuthenticated = False
                curr_session = ""
            else:
                isAlive = False


def StorageAPI():
    global file_name, file_whereabout
    isAlive = True

    while isAlive:
        print("1: отправка файла;")
        print("2: получение файла;")
        print("3: удаление файла.")

        inp = int(input())

        if inp == 1:
            try:
                file_whereabout = input("Введите путь до файла: ")
            except Exception as e:
                print("Введите корректную строку")
                return

            result = post_file(url, file_whereabout)

            print(result)

        elif inp == 2:
            try:
                file_name = input("Введите название файла: ")
            except Exception as e:
                print("Введите корректную строку")
                return

            result = get_file(url, file_name)

            print(result)

        elif inp == 3:
            try:
                file_name = input("Введите название файла: ")
            except Exception as e:
                print("Введите корректную строку")

            result = delete_file(url, file_name)

            print(result)
        else:
            isAlive = False


if __name__ == '__main__':
    inp = int(input("1 - NotebookAPI, остальное - StorageAPI : "))
    if inp == 1:
        NotebookAPI()
    else:
        StorageAPI()