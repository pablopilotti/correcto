import random
from collections import defaultdict
from random import shuffle
from operator import itemgetter, attrgetter, methodcaller
import itertools

s00 = range(1, 91)
s1 = [22, 84, 23, 69, 83, 2, 70, 42, 24, 44, 21, 46, 55, 61, 5, 19, 26, 60, 90, 3, 64, 15, 76, 49, 68, 18, 72, 67, 51,
      12, 74, 48, 52, 65, 59, 1, 40, 10, 75, 66, 30, 63, 28, 29, 58, 73, 4, 41, 45, 57, 82, 20, 34, 32, 36]
s2 = [42, 14, 43, 68, 6, 3, 16, 80, 27, 41, 56, 21, 32, 36, 57, 87, 22, 62, 15, 26, 11, 18, 72, 61, 19, 40, 65, 50, 60,
      49, 28, 81, 79, 64, 84, 46, 9, 89, 86, 58, 74, 88, 85, 7, 75, 59, 70, 55, 52, 52, 4, 63, 1, 25, 44, 5, 77, 37]
s3 = [34, 68, 13, 33, 58, 74, 10, 75, 5, 62, 60, 79, 14, 76, 66, 7, 40, 70, 90, 89, 63, 41, 32, 44, 55, 38, 69, 8, 4,
      49, 39, 73, 26, 87, 72, 22, 18, 51, 84, 15, 28, 16, 53, 52, 25, 88, 56]
s4 = [59, 64, 6, 68, 72, 10, 44, 80, 34, 51, 56, 69, 45, 77, 42, 9, 5, 73, 82, 24, 28, 19, 53, 37, 3, 61, 36, 66, 58,
      49, 27, 52, 63, 87, 16, 46, 29, 2, 75, 21, 30, 83, 15, 39, 13, 62, 14, 22, 90, 79]
s5 = [50, 39, 61, 45, 28, 44, 58, 25, 63, 41, 85, 49, 23, 43, 4, 6, 70, 72, 36, 17, 71, 5, 48, 74, 29, 51, 76, 65, 64,
      3, 66, 38, 1, 52, 78, 57, 15, 26, 24, 37, 90, 79, 59, 11, 12, 16, 33, 31, 7, 87, 47]
s6 = [12, 2, 24, 20, 86, 60, 34, 71, 37, 64, 14, 35, 30, 79, 28, 42, 26, 69, 65, 63, 49, 23, 36, 7, 8, 66, 76, 51, 40,
      29, 83, 84, 73, 6, 68, 67, 1, 90, 50, 32, 18, 15, 3, 25, 31, 87, 70, 55, 48, 62, 19, 74, 39, 54]
s7 = [6, 52, 39, 77, 1, 43, 68, 82, 40, 30, 84, 25, 53, 41, 89, 48, 72, 67, 87, 20, 64, 57, 61, 49, 75, 2, 46, 42, 58,
      45, 36, 8, 31, 63, 90, 5, 3, 28, 18, 9, 13, 4, 37, 69, 60, 71, 51, 65, 33, 16, 47]
s8 = [16, 50, 76, 84, 14, 53, 40, 4, 63, 23, 10, 65, 8, 79, 51, 64, 67, 42, 7, 60, 70, 29, 80, 28, 62, 38, 89, 37, 21,
      43, 15, 73, 34, 58, 39, 83, 13, 22, 3, 11, 85, 57, 55, 52, 27, 19, 44, 72, 17, 69, 24, 82, 1]
s9 = [76, 16, 7, 48, 36, 90, 86, 42, 18, 55, 37, 11, 69, 54, 67, 78, 14, 82, 41, 88, 25, 58, 8, 63, 46, 31, 75, 49, 80,
      10, 32, 34, 84, 77, 53, 2, 81, 13, 50, 47, 28, 73, 1, 39, 38, 68, 29, 51]
s10 = [20, 26, 75, 19, 7, 76, 5, 43, 50, 60, 90, 15, 6, 31, 79, 71, 70, 3, 88, 86, 83, 8, 84, 48, 67, 46, 35, 45, 63,
       17, 42, 52, 73, 27, 62, 29, 69, 9, 32, 74, 66, 10, 22, 82, 1, 13, 64, 53, 4, 87]
s11 = [81, 58, 19, 38, 47, 74, 12, 17, 18, 71, 62, 69, 60, 39, 25, 46, 40, 52, 76, 21, 1, 55, 35, 33, 10, 73, 51, 15,
       20, 36, 68, 79, 27, 11, 63, 88, 83, 22, 72, 4, 66, 85, 37, 49]
s12 = [44, 74, 21, 80, 56, 63, 13, 11, 55, 12, 77, 20, 17, 33, 3, 67, 58, 26, 49, 25, 68, 41, 87, 8, 81, 51, 72, 71, 53,
       90, 9, 62, 28, 70, 18, 69, 76, 82, 61, 47, 88, 46, 84, 16, 65, 60, 66, 36, 45]
s13 = [2, 31, 26, 81, 48, 40, 45, 83, 25, 22, 84, 78, 37, 21, 6, 42, 17, 79, 39, 68, 30, 18, 20, 36, 11, 16, 1, 24, 43,
       7, 77, 38, 27, 14, 5, 59, 12, 60, 3, 66, 10, 85, 69, 76, 73, 89, 62, 63, 70, 56, 61]
s14 = [45, 84, 9, 33, 19, 75, 86, 31, 27, 56, 20, 58, 85, 87, 79, 38, 37, 70, 71, 64, 53, 39, 34, 35, 61, 43, 57, 69,
       47, 49, 11, 76, 15, 13, 41, 66, 30, 72, 68, 89, 78, 6, 55, 28, 8, 54, 67, 7]
s15 = [10, 60, 40, 25, 76, 52, 49, 32, 19, 9, 79, 90, 83, 39, 70, 3, 11, 64, 84, 53, 21, 33, 34, 6, 65, 48, 13, 14, 4,
       74, 20, 1, 41, 42, 81, 57, 75, 50, 66, 44, 15, 78, 38, 51, 69, 45, 47, 22]
s16 = [7, 70, 39, 31, 13, 17, 88, 10, 43, 80, 4, 26, 19, 63, 49, 22, 6, 20, 65, 50, 85, 54, 35, 44, 58, 15, 41, 81, 1,
       76, 40, 71, 79, 38, 46, 47, 75, 5, 74, 55, 89, 29, 16, 87, 12, 57, 59, 62, 90, 27]
s17 = [11, 87, 18, 78, 72, 24, 76, 28, 34, 86, 74, 37, 38, 56, 21, 47, 77, 66, 57, 51, 33, 63, 84, 9, 8, 83, 44, 69, 36,
       15, 46, 19, 62, 67, 68, 10, 42, 50, 88, 54, 16, 43, 26, 55, 82, 60, 64, 49, 41, 22, 61, 52, 81, 4]
s18 = [31, 35, 10, 37, 78, 51, 17, 87, 3, 18, 71, 48, 26, 66, 9, 64, 40, 54, 5, 45, 57, 29, 1, 55, 14, 65, 4, 74, 85,
       90, 32, 30, 27, 46, 89, 12, 24, 77, 38, 81, 33, 82, 56, 7, 44, 21, 59, 39, 23, 34, 80]
s19 = [37, 68, 48, 86, 39, 42, 62, 41, 56, 59, 13, 63, 27, 43, 70, 29, 87, 9, 71, 79, 10, 2, 85, 8, 35, 31, 22, 33, 18,
       6, 64, 69, 82, 75, 45, 67, 21, 25, 34, 89, 53, 90, 40, 88, 7, 54, 30, 24, 55, 20, 52, 78]
s20 = [7, 68, 80, 1, 45, 83, 21, 30, 65, 6, 9, 88, 15, 67, 72, 50, 20, 86, 22, 13, 77, 47, 57, 52, 34, 54, 87, 23, 85,
       5, 38, 66, 81, 40, 29, 74, 70, 56, 36, 78, 28, 60, 53, 59, 33, 89, 27, 8, 41, 62, 16, 48]
s21 = [42, 69, 31, 11, 62, 86, 16, 66, 28, 84, 37, 34, 27, 24, 85, 3, 83, 20, 9, 21, 10, 89, 25, 6, 17, 82, 90, 57, 65,
       29, 52, 32, 63, 38, 50, 12, 4, 88, 67, 58, 19, 80, 22, 23, 70, 77, 59, 55, 81, 45, 51, 41, 40]
s22 = [36, 78, 90, 69, 45, 83, 89, 47, 75, 14, 6, 22, 40, 85, 67, 46, 34, 12, 28, 8, 55, 50, 88, 43, 82, 19, 87, 18, 48,
       1, 53, 58, 81, 29, 64, 13, 60, 31, 44, 59, 65, 56, 23, 30, 42, 33, 25, 49, 37]

columnas = \
    [[[list(x) for x in itertools.combinations(range(9, 0, -1), 0)],
      [list(x) for x in itertools.combinations(range(9, 0, -1), 1)],
      [list(x) for x in itertools.combinations(range(9, 0, -1), 2)],
      [list(x) for x in itertools.combinations(range(9, 0, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(19, 9, -1), 0)],
      [list(x) for x in itertools.combinations(range(19, 9, -1), 1)],
      [list(x) for x in itertools.combinations(range(19, 9, -1), 2)],
      [list(x) for x in itertools.combinations(range(19, 9, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(29, 19, -1), 0)],
      [list(x) for x in itertools.combinations(range(29, 19, -1), 1)],
      [list(x) for x in itertools.combinations(range(29, 19, -1), 2)],
      [list(x) for x in itertools.combinations(range(29, 19, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(39, 29, -1), 0)],
      [list(x) for x in itertools.combinations(range(39, 29, -1), 1)],
      [list(x) for x in itertools.combinations(range(39, 29, -1), 2)],
      [list(x) for x in itertools.combinations(range(39, 29, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(49, 39, -1), 0)],
      [list(x) for x in itertools.combinations(range(49, 39, -1), 1)],
      [list(x) for x in itertools.combinations(range(49, 39, -1), 2)],
      [list(x) for x in itertools.combinations(range(49, 39, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(59, 49, -1), 0)],
      [list(x) for x in itertools.combinations(range(59, 49, -1), 1)],
      [list(x) for x in itertools.combinations(range(59, 49, -1), 2)],
      [list(x) for x in itertools.combinations(range(59, 49, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(69, 59, -1), 0)],
      [list(x) for x in itertools.combinations(range(69, 59, -1), 1)],
      [list(x) for x in itertools.combinations(range(69, 59, -1), 2)],
      [list(x) for x in itertools.combinations(range(69, 59, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(79, 69, -1), 0)],
      [list(x) for x in itertools.combinations(range(79, 69, -1), 1)],
      [list(x) for x in itertools.combinations(range(79, 69, -1), 2)],
      [list(x) for x in itertools.combinations(range(79, 69, -1), 3)]],
     [[list(x) for x in itertools.combinations(range(90, 79, -1), 0)],
      [list(x) for x in itertools.combinations(range(90, 79, -1), 1)],
      [list(x) for x in itertools.combinations(range(90, 79, -1), 2)],
      [list(x) for x in itertools.combinations(range(90, 79, -1), 3)]],
     ]


def get_col(n, m, column):
    ret = column[n][m].pop(0)
    column[n][m].append(ret)
    return ret


def set_config2(n):
    if n == 0:
        return [0]
    ret = []
    for i in range(n):
        
        ret.append([i, set_config2(i)])
    return ret


def set_config():
    conf = []
    for i0 in range(1, 4):
        for i1 in range(1, 4):
            for i2 in range(1, 4):
                for i3 in range(1, 4):
                    for i4 in range(1, 4):
                        for i5 in range(1, 4):
                            for i6 in range(1, 4):
                                for i7 in range(1, 4):
                                    for i8 in range(1, 4):
                                        if i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 == 15:
                                            config = [i0, i1, i2, i3, i4, i5, i6, i7, i8]
                                            cant = 1
                                            for i in range(0, len(config)):
                                                cant *= len(columnas[i][config[i]-1])
                                            conf.append([i0, i1, i2, i3, i4, i5, i6, i7, i8, cant])
    return conf


def mezclar(conf, column):
    shuffle(conf)
    for cols in column:
        for c in cols:
            shuffle(c)
    return


def get_conf(conf):
    ret = conf.pop(0)
    conf.append(ret)
    return ret


def crear_cartones(cant, conf, column):
    mezclar(conf, column)
    cartones = []
    while len(cartones) < cant:
        c = get_conf(conf)
        carton = []
        for i in range(0, len(columnas)):
            carton.append(get_col(i, c[i], column))
        cartones.append(carton)
    return cartones

# dic = {}
# dic = defaultdict(lambda: 0, dic)
# for carton in cartones:
#     for col in carton:
#         for num in col:
#             dic[num] += 1
# print dic


def jugar(cartones, sorteo):
    ganadores = []
    num = 30
    while num < len(sorteo) and len(ganadores) == 0:
        for carton in cartones:
            if all(set(col) < set(sorteo[:num]) for col in carton):
                # print carton, num, len(sorteo)
                ganadores.append(carton)
        num += 1
    return ganadores, num-1

# for s in range(len(sorteo)):
#     print 'sorteo ', s
#     jugar(cartones, sorteo[s])

############################################
# Main
# for cartones_size in range(20000, 30000, 2000):
configuraciones = set_config()
cartones = crear_cartones(30000, configuraciones, columnas)
for carton in cartones:
    for columna in carton:
        for numero in columna:
            print numero,
    print
    # gan_prom = 0
    # lon_prom = 0
    # for s in range(100):
    #     shuffle(s00)
    #     ganadores, num = jugar(cartones, s00)
    #     gan_prom += len(ganadores)
    #     lon_prom += num
    # print 'cartones:', cartones_size, 'ganadores:', gan_prom, 'longitud:', lon_prom
    #
# for m in range(10):
# for m in range(10):
#     print 'sorteo:', m
#     s = shuffle(s00)

# def carton():
#     conf = False
#     while len(configuraciones) != 0 and not conf:
#         n = random.randrange(0, len(configuraciones))
#         p = configuraciones[n]
#         conf = True
#         l = []
#         for i in range(9):
#             l.append(len(columnas[i][p[i] - 1]))
#             if l[i] == 0:
#                 # print i, p
#                 configuraciones.remove(p)
#                 conf = False
#                 break
#
#     if len(configuraciones) == 0:
#         return []
#
#     cart = []
#     for i in range(9):
#         ni = random.randrange(0, l[i])
#         elem = columnas[i][p[i] - 1][ni]
#         cart.append(elem)
#         columnas[i][p[i] - 1].remove(elem)
#     print cart
#     return cart


# count = 0
# while carton():
#     count += 1
# print count
#
# for i in range(0, 9):
#     for j in range(0,3):
#         print i, j, len(columnas[i][j])

# print columnas
