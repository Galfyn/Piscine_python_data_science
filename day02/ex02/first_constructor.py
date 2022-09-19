from sys import argv


class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as f:
            return f.read()


def hand_argv(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        if len(line) < 2 or len(line[0].split(',')) != 2:
            raise Exception("Error struct file")
        for i in range(1, len(line) - 1):
            if line[i] != '0,1\n' and line[i] != '1,0\n':
                raise Exception("Error struct file")


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception("Error argument")
    text = Research(argv[1])
    print(text.file_reader())
