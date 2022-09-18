import sys


class Research:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as f:
            return f.read()


def hand_argv(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        if len(line) < 2 or len(line[0].split(',')) != 2:
            raise Exception("Error argument")
        for i in range(1, len(line) - 1):
            if line[i] != '0,1\n' and line[i] != '1,0\n':
                raise Exception("Error argument")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Error argument")
    print(Research(sys.argv[1]))

