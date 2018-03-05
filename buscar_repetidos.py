#!/usr/bin/env python

import argparse
import sys


def main(argv=sys.argv[1:]):
    """
    Buscar cartones de bingo repetidos
    """

    parser = argparse.ArgumentParser(
        description='Buscar cartones de bingo repetidos.')
    parser.add_argument('-f', '--file', required=True,
                        help='Archivo con cartones de bingo')
    args = parser.parse_args(argv)

    fh = open(args.file)
    cartones = []
    repetidos = 0
    for line in fh:
        c = map(int, line.strip('\n').rstrip(' ').split(' '))
        if c not in cartones:
            cartones.append(c)
        else:
            # print args.file, "Carton repetido ", c
            repetidos += 1
    print args.file, "Cartones repetidos: ", repetidos
    fh.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
