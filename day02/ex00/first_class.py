

def data():
    filename = 'data.csv'
    lst = [
        ('head', 'tail'),
        ('0', '1'),
        ('1', '0'),
        ('0', '1'),
        ('1', '0'),
        ('0', '1'),
        ('0', '1'),
        ('0', '1'),
        ('1', '0'),
        ('1', '0'),
        ('0', '1'),
        ('1', '0'),
    ]
    with open(filename, 'w') as f:
        for t in lst:
            f.write(','.join(str(s) for s in t) + '\n')
    return filename


class MustRead:
    with open(data(), 'r') as f:
        print(f.read())


if __name__ == '__main__':
    pass
