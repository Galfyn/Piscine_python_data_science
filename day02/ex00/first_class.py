

def data():
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
    with open('data.csv', 'w+') as f:
        for t in lst:
            f.write(','.join(str(s) for s in t) + '\n')


class MustRead:
    data()
    with open('data.csv', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    MustRead()
