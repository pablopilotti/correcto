#!/usr/bin/env python

import argparse
import sys


def main(argv=sys.argv[1:]):
    """
    Ordenador de cartones de bingo
    """

    parser = argparse.ArgumentParser(
        description='Ordenador de cartones de bingo.')
    parser.add_argument('-f', '--file', required=True,
                        help='Archivo con cartones de bingo')
    args = parser.parse_args(argv)

    fh = open(args.file)
    for line in fh:
        for num in sorted(map(int, line.strip('\n').rstrip(' ').split(' '))):
            print str(num).zfill(2),
        print
    fh.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
