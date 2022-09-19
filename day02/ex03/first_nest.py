from sys import argv


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
        def counts(lst_list):
            heads = 0
            tails = 0
            for i in range(len(lst_list)):
                if lst_list[i][0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        def fractions(lst_count):
            sum_count = lst_count[0] + lst_count[1]
            return lst_count[0] / sum_count, lst_count[1] / sum_count


def check_arg(path):
    with open(path, 'r') as file:
        line = file.readlines()
        if len(line) == 0 or (len(line) == 1 and (line[0] != '0,1\n' and line[0] != '1,0\n')):
            raise Exception("Error file")
        if len(line) > 1:
            for i in range(1, len(line) - 1):
                if line[i] != '0,1\n' and line[i] != '1,0\n':
                    raise Exception("Error file")


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception("Error argument")
    list_lists = Research(argv[1]).file_reader()
    print(list_lists)
    list_counts = Research.Calculations.counts(list_lists)
    print(list_counts[0], list_counts[1])
    list_fractions = Research.Calculations.fractions(list_counts)
    print(list_fractions[0], list_fractions[1])
