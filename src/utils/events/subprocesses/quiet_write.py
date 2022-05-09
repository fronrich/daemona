# write string to a file in parallel
# takes two parameters

import sys


def main():
    data = sys.argv[1]
    path = sys.argv[2]
    textfile = open(path, "w")
    a = textfile.write(data)
    textfile.close()
    return a


main()
