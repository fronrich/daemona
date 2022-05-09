import sys
import os


def main():
    path = sys.argv[1]
    os.remove(path)


main()
