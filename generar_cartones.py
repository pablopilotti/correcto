#!/usr/bin/env python

import random
from collections import defaultdict
from random import shuffle
from operator import itemgetter, attrgetter, methodcaller
import itertools
import argparse
import sys


def get_cols(maximo, nonclassic):
    cols = []
    if nonclassic:
        for i in range(10, 100, 10):
            c = []
            for j in range(0, maximo+1):
                c.append([list(x) for x in
                          itertools.combinations(range(i, i-10, -1), j)])
            cols.append(c)
        return cols
    else:
        c = []
        for j in range(0, maximo + 1):
            c.append([list(x) for x in
                      itertools.combinations(range(9, 0, -1), j)])
        cols.append(c)
        for i in range(19, 89, 10):
            c = []
            for j in range(0, maximo+1):
                c.append([list(x) for x in
                          itertools.combinations(range(i, i-10, -1), j)])
            cols.append(c)
        c = []
        for j in range(0, maximo + 1):
            c.append([list(x) for x in
                      itertools.combinations(range(90, 79, -1), j)])
        cols.append(c)
        return cols


def set_config(max):
    conf = []
    for i0 in range(1, max + 1):
        for i1 in range(1, max + 1):
            for i2 in range(1, max + 1):
                for i3 in range(1, max + 1):
                    for i4 in range(1, max + 1):
                        for i5 in range(1, max + 1):
                            for i6 in range(1, max + 1):
                                for i7 in range(1, max + 1):
                                    for i8 in range(1, max + 1):
                                        if i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 == 15:
                                            conf.append([i0, i1, i2, i3, i4, i5, i6, i7, i8])
    return conf


def shuffle_all(conf, column):
    shuffle(conf)
    for cols in column:
        for c in cols:
            shuffle(c)
    return


def get_and_roll(vect):
    ret = vect.pop(0)
    vect.append(ret)
    return ret


def make_bingos(cant, conf, column):
    shuffle_all(conf, column)
    bingos = []
    size = 0
    while size < cant:
        c = get_and_roll(conf)
        b = []
        for i in range(0, len(column)):
            b.append(get_and_roll(column[i][c[i]]))
        bingos.append(b)
        size += 1
    return bingos


def generate(size, max, nonclassic):
    configs = set_config(max)
    columns = get_cols(max, nonclassic)

    bingos = make_bingos(size, configs, columns)
    for bingo in bingos:
        for col in bingo:
            for num in col:
                print str(num).zfill(2),
        print
    return 0


def main(argv=sys.argv[1:]):
    """
    Generador de cartones de bingo
    """

    parser = argparse.ArgumentParser(
        description='Generador de cartones de bingo.')
    parser.add_argument('-c', '--cantidad', help='Cantidad de cartones a generar')
    parser.add_argument('-m', '--maximo', help='Maximo de numeros por columna. (2 o 3)')
    parser.add_argument('-n', '--noClasico', action="store_true",
                        help='10 posibles numeros por casillero')

    args = parser.parse_args(argv)
    if not args.cantidad:
        print 'Debe especificarse una cantidad de cartones a generar.'
        parser.print_help()
        sys.exit(1)

    if not args.maximo or int(args.maximo) < 2 or int(args.maximo) > 3:
        print 'Debe especificarse una maximo de numeros por columna (2 o 3).'
        parser.print_help()
        sys.exit(1)

    ret = generate(int(args.cantidad), int(args.maximo), args.noClasico)
    sys.exit(ret)


if __name__ == '__main__':
    main()