from random import randint
from config import *


class Research:
    def __init__(self, path):
        self.filename = path

    def file_reader(self, has_header=True):
        with open(self.filename, 'r') as f:
            line = f.readlines()
            if line[0] == '0,1\n' or line[0] == '1,0\n':
                self.has_header = False
            start = 0
            if has_header:
                start = 1
            lst_list = []
            for i in range(start, len(line)):
                lst_i = [int(line[i][0])]
                lst_i.append(int(line[i][2]))
                lst_list.append(lst_i)
            return lst_list

    class Calculations:
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(self):
            return [(self.count[0] / (self.count[0] + self.count[1])) * 100,
                    (self.count[1] / (self.count[0] + self.count[1])) * 100]

    class Analytics(Calculations):
        def __init__(self, n_steps):
            self.n_steps = n_steps
            self.predict = self.predict_random()
            self.predict_last = self.predict_last()
            self.count = self.counts()

        def predict_random(self):
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(self.n_steps)]

        def counts(self):
            x = [x[0] for x in self.predict]
            y = [y[1] for y in self.predict]
            return [sum(x), sum(y)]

        def predict_last(self):
            if not len(self.predict):
                print("Enter the correct number of trials")
            else:
                return self.predict[-1]

        def save_file(report, REPORT_FILE, EXTENSION):
            with open(f'{REPORT_FILE}.{EXTENSION}', 'w') as report_file:
                report_file.write(report)