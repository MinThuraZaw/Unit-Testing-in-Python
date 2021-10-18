import os


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception('Bad file!')

    file = open(filename, 'r')
    line = file.readline()
    return line
