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
                curr_session = post_user(url)
                if (len(curr_session) > 0):
                    isAuthenticated = True
            elif inp == 2:
                curr_session = get_login(url)
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
                get_user(curr_session, url)
            elif inp == 2:
                post_todo(curr_session, url)
            elif inp == 3:
                get_todo(curr_session, url)
            elif inp == 4:
                put_todo(curr_session, url)
            elif inp == 5:
                delete_todo(curr_session, url)
            elif inp == 6:
                isAuthenticated = False
                curr_session = ""
            else:
                isAlive = False


def StorageAPI():
    isAlive = True

    while isAlive:
        inp = int(input())

        if inp == 1:
            post_file(url)
        elif inp == 2:
            get_file(url)
        elif inp == 3:
            delete_file(url)
        else:
            isAlive = False


if __name__ == '__main__':
    inp = int(input("1 - NotebookAPI, остальное - StorageAPI : "))
    if inp == 1:
        NotebookAPI()
    else:
        StorageAPI()