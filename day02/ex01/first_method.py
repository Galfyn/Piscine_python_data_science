
class Research:
    def file_reader(self):
        with open('../ex00/data.csv', 'r') as f:
            return f.read()


if __name__ == '__main__':
    res = Research()
    print(res.file_reader())
