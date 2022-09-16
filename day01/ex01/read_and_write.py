

def read_and_write(filename):
    input_file = open(filename + '.csv', 'r')
    output_file = open(filename + '.tsv', 'w')
    output_file.write(input_file.read().replace('",', '"\t'))


if __name__ == '__main__':
    read_and_write('ds.csv')