"""
https://repl.it/@MarinaKrvtsn/JSONfile-1#main.py has .json

Разработать фрагмент программы, который будет сохранять вводимые пользователем данные, по выбору в json, или csv-файле (использовать модули csv, json) с использованием протокола менеджеров контекста, а также расширенного синтаксиса исключений.
"""

no_json = False
try:
    import json
except ImportError:
    no_json = True
   
from texttable import Texttable


def main():
    con = "y"
    credentials = []
    while(con == "y"):
        username = input("username: ")
        password = input("password: ")
        dataofuser = {"username": username,"password": password}
        credentials.append(dataofuser)
        con = input("continue? (y/n)")
    dataset = {"users": credentials}
    inputInFile(dataset)


def inputInFile(*data): 
    try:
        with open('data.json', 'w') as f:
            try:
                json.dump(data, f, sort_keys=True, indent=2)
                print("recorded")
            except json.Error as e:
                print("error", e)
                return None
    except FileNotFoundError as e:
        print("no file ", e)
        return None

main()

# jsonread('data.txt')

if __name__ == "__main__":

    def test1():
        print('test1 is running')
        try:
            assert no_json == True, "ImportError"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")
    
    
    import pytest
    def test2():
        with pytest.raises(KeyError):
            data.pop(2020) # IndexError: pop index out of range

    
    import doctest
    doctest.testmod()

    # test1()
    # test2()
