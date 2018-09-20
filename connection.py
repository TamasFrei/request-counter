def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for request in data:
            row = request + ': ' + str(data[request]) + '\n'
            file.write(row)


def read_file(filename):
    counter = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for row in lines:
            line = row.split(': ')
            counter[line[0]] = int(line[1])
    return counter


