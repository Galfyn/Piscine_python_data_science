#!python3
import timeit
from functools import reduce
from sys import argv


def get_n():
    if len(argv) == 4 and argv[3].isdigit():
        return int(argv[3])


def loop_sqrt_sum(n: int = get_n()):
    if not n:
        return
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


def reduce_sqrt_sum(n: int = get_n()):
    if not n:
        return

    def func(x, y):
        return x + y * y

    return reduce(func, range(1, n + 1))


def benchmark():
    func_dict = {'loop': 'loop_sqrt_sum', 'reduce': 'reduce_sqrt_sum'}

    if argv[1] in func_dict and argv[2].isdigit() and argv[3].isdigit():
        time = timeit.timeit(f'{func_dict[argv[1]]}()',
                             f'from __main__ import {func_dict[argv[1]]}',
                             number=int(argv[2]))
        print(time)
    else:
        print('Bad Argument')


if __name__ == "__main__":
    if len(argv) != 4:
        raise Exception("Error argument")
    benchmark()
