# Домашнее задание к лекции 1.«Import. Module. Package»
# main.py
from application.salary import calculate_salary
from application.db.people import get_employees


def timing():
    from datetime import datetime as dt
    return dt.now().strftime("%d.%m.%Y %H:%M:%S")


if __name__ == '__main__':
    print(f'run {timing()} => main;')
    print(f'run {timing()} =>', end=' ')
    calculate_salary()
    print(f'run {timing()} =>', end=' ')
    get_employees()
