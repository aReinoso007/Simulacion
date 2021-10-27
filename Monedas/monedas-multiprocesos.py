from multiprocessing import Process
import random as r
import collections
import matplotlib.pyplot as plt
import time
import numpy as np
from numpy.core.records import array

A = []
B = []
iteraciones = [100, 1000, 10000, 100000]
N = 100
sumatoria = []
for i in range(N):
    sumatoria.append(i)
counter = []


def setup():
    for i in range(N):
        a = r.randint(1, 6)
        A.append(a)
        b = r.randint(1, 6)
        B.append(b)


def sumar(V1, V2, N1, N2):
    sum = 0
    for i in range(int(N1), int(N2)):
        sum = V1[i]+V2[i]
        print('suma: ', sum)
        sumatoria[i] += sum


if __name__ == '__main__':
    setup()
    print('sum len: ', len(sumatoria))
    tInit = time.time()

    # iteraciones solo funcionan en #%4
    # 0-25%
    # 25%-50%
    # 50%-75%
    # 75%-100%

    p1 = Process(target=sumar, args=(A, B, int(0), int(N*(1/4))))
    p2 = Process(target=sumar, args=(A, B, int(N*(1/4)), int(N*(2/4))))
    p3 = Process(target=sumar, args=(A, B, int(N*(2/4)), int(N*(3/4))))
    p4 = Process(target=sumar, args=(A, B, int(N*(3/4)), int(N)))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    counter = collections.Counter(sumatoria)
    print('frecuencia: ', counter)
    plt.bar(counter.keys(), counter.values())
    plt.show()


# posible solucion, subproceso que recoja cada sumatoria y le agregue
# vector de uno en uno por cada proceso
