#!python3
import timeit
from sys import argv


def get_mail_list():
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5


def loop_list():
    mail_list = get_mail_list()
    result = []
    for i in mail_list:
        if i.find('@gmail.com') != -1:
            result.append(i)
    return result


def compr_list():
    mail_list = get_mail_list()
    return [i for i in mail_list if i.find('@gmail.com') != -1]


def map_list():
    mail_list = get_mail_list()

    def map_func(mail):
        if mail.find('gmail.com') != -1:
            return mail
    result = map(map_func, mail_list)
    # result = list(map(map_func, mail_list))
    return result


def filter_list():
    mail_list = get_mail_list()

    def filter_func(mail):
        if mail.find('gmail.com'):
            return True
        else:
            return False
    result = filter(filter_func, mail_list)
    return result


def benchmark():
    func_dict = {'list_comprehension': 'compr_list',
                 'loop': 'loop_list',
                 'map': 'map_list',
                 'filter': 'filter_list'}

    if argv[1] in func_dict and argv[2].isdigit():
        time = timeit.timeit(f'{func_dict[argv[1]]}()', f'from __main__ import {func_dict[argv[1]]}', number=int(argv[2]))
        print(time)
    else:
        print('Bad Argument')


if __name__ == "__main__":
    if len(argv) != 3:
        raise Exception("Error argument")
    benchmark()
