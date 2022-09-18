
class Research:
    def file_reader(self):
        with open('../ex00/data.csv', 'r') as f:
            text = f.read()
            return text


if __name__ == '__main__':
    Res = Research()
    print(Res.file_reader())
