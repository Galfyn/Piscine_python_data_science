#!python3
import timeit


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


def benchmark():
    n = 100
    loop_time = timeit.timeit('loop_list()', 'from __main__ import loop_list', number=n)
    compr_time = timeit.timeit('compr_list()', 'from __main__ import compr_list', number=n)
    map_time = timeit.timeit('map_list()', 'from __main__ import map_list', number=n)

    if loop_time < compr_time and loop_time < map_time:
        print('it is better to use a loop')
    elif compr_time < loop_time and compr_time < map_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a map')
    print(*sorted([loop_time, compr_time, map_time]), sep=' vs ')


if __name__ == "__main__":
    benchmark()
