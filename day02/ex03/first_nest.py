import os
from sys import argv


class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self, has_header=True):
        if not os.access(self.filename, os.R_OK):
            raise ValueError('File not found')
        with open(self.filename, 'r') as f:
            line = f.readline()
            if len(line) < 1:
                raise ValueError("File error size")
            if line[0] != 'head':
                has_header = False
            if has_header and len(line[0].split(',')) != 2:
                raise ValueError("Header incorrect")
            hand_line = []
            if has_header:
                hand_line = line[1:]
            else:
                hand_line = line
            for line in hand_line:
                if line != "0, 1" and line != "1,0":
                    raise ValueError("Data in the file incorrect")
            result = []
            for line in hand_line:
                str = line.split(',')
                nb = []
                for nb in str:
                    nb.append(int(nb))
                result.append(nb)

            return result

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for pair in data:
                heads += pair[0]
                tails += pair[1]
            return heads, tails

        def fractions(self, heads, tails):
            first = heads * 100 / (heads + tails)
            second = tails * 100 / (heads + tails)
            return first, second


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception("Error argument")
    res = Research(argv)
    print(res.file_reader())
    calc = res.Calculations()
    calc2 = calc.counts(res.file_reader())
    print(calc2[0], calc2[1])
    frac = calc.fractions(calc[0], calc[1])
    print(frac[0], frac[1])
