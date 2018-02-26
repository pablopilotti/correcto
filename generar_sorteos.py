#!/usr/bin/env python

from random import shuffle
import argparse
import sys


def generate(cant):
    sorteo = range(1, 91)
    i = 0
    while i < cant:
        i += 1
        shuffle(sorteo)
        for s in sorteo:
            print str(s).zfill(2),
        print
    return 0


def main(argv=sys.argv[1:]):
    """
    Generador de sorteos de bingo
    """

    parser = argparse.ArgumentParser(
        description='Generador de sorteos de bingo.')
    parser.add_argument('-c', '--cantidad', help='Cantidad de sorteos a generar')

    args = parser.parse_args(argv)
    if not args.cantidad:
        print 'Debe especificarse una cantidad de sorteos a generar.'
        parser.print_help()
        sys.exit(1)

    ret = generate(int(args.cantidad))
    sys.exit(ret)


if __name__ == '__main__':
    main()