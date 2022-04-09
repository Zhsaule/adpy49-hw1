# Домашнее задание к лекции 1.«Import. Module. Package»
# dirty_main.py
# *4. Создать рядом с файлом main.py модуль dirty_main.py
# и импортировать все функции с помощью конструкции (необязательное задание)
from application.salary import *
from application.db.people import *


def timing():
    from datetime import datetime as dt
    return dt.now().strftime("%d.%m.%Y %H:%M:%S")


if __name__ == '__main__':
    print(f'run {timing()} => dirty_main;')
    print(f'run {timing()} =>', end=' ')
    calculate_salary()
    print(f'run {timing()} =>', end=' ')
    get_employees()
