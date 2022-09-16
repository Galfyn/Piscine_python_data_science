def data_types():
    i = 1  # Int
    s = "str"  # String
    f = 5.55  # Float
    b = False  # Bool
    l = ['10', '15']  # Лист
    d = {'key': 10, 'key2': 12}  # Словарь
    t = ('string', 123, True)  # Кортеж (Неизменяемый список)
    se = set(t)  # Множество

    arr = [type(i).__name__, type(s).__name__, type(f).__name__, type(b).__name__,
           type(l).__name__, type(d).__name__, type(t).__name__, type(se).__name__]
    print(arr)


if __name__ == '__main__':
    data_types()
