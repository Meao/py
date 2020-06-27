"""
Инвариантная самостоятельная работа (ИСР)

4.1. Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран. Организовать тестирование работоспособности программы с помощью assert, print.

Список исключительных ситуаций, которые могут возникнуть:

отсутствие модуля json и/или pprint  (ImportError);
отсутствие файла (FileNotFoundError);
ошибка в структуре JSON, включая отсутствие содержимого файла (JSONDecodeError);
в каких ситуациях может возникнуть IOError?
KeyError и/или IndexError в случае непрофессионального итерирования по объекту, взятия значений по ключам;
подумать, есть ли ещё?
4.2. Дополнение программы задания 4.1 (считывание данных JSON-формата) тестами с использованием библиотеки doctest.

4.3. Дополнение программы задания 4.1,4.2 (считывание данных JSON-формата) тестами с использованием пакета py.test.

4.4. Формирование отчета по самостоятельно работе и публикация его в портфолио.
"""

no_json = False
try:
    import json
except ImportError:
    no_json = True
   
import pandas as pd

def jsonread(filename):
    """
    Testing jsonread 

    Made some test for jsonread executing 

    >>> jsonread('data.txt')
                            _id  ...  name.l                        _id  ...  name.l
    ast                                     0  5ebabaeb564bc1ed532f6948  ...      Br
    ock                                     1  5ebabaebc39273283a602ef5  ...    Roll
    ins                                     2  5ebabaebbdb974907114dfce  ...   Bartl
    ett                                     3  5ebabaebadc115d3017bd49f  ...   Melen
    dez                                     4  5ebabaeb8fd85e5e46638141  ...       B
    ird                                     5  5ebabaeb853c00ae425e4b95  ...    Vinc
    ent                                     6  5ebabaeb257320c9bebc3470  ...    Sanf
    ord                                     7  5ebabaebd52da660055cade4  ...       L
    owe                                     8  5ebabaeb82efd5f42192d1b6  ...    Hubb
    ard                                     9  5ebabaebca42c48c77d7a4ed  ...      Se
    ars

    [10 rows x 23 columns]
    """    
    res = None

# https://docs.python.org/3/library/json.html
with open('data.txt') as json_file:
    data = json.load(json_file)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#normalization
    print(pd.json_normalize(data))

if __name__ == "__main__":

    def test1():
        print('test1 is running')
        try:
            assert no_json == True, "ImportError"
        except AssertionError as e:
             print(f"ошибка была такая: {e}")
    
    
    import pytest
    def test5():
        with pytest.raises(KeyError):
            data.pop(2016) # IndexError: pop index out of range

    
    import doctest
    doctest.testmod()

    test1()
    test5()
