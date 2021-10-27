import random as r
import collections
import matplotlib.pyplot as plt

A = []
B = []
sumatoria = []

Valores = [100, 1000, 10000, 100000]
print('1er valor: ', Valores[2])

for j in range(0, len(Valores)):
    sumatoria.clear()
    for i in range(Valores[j]):
        a = r.randint(1, 6)
        a = r.randint(1, 6)
        A.append(a)
        b = r.randint(1, 6)
        B.append(b)
        sumatoria.append(a+b)
    counter = collections.Counter(sumatoria)
    print('Frecuencias: ', counter)
    plt.bar(counter.keys(), counter.values())
    plt.title('Frecuencia-%s' % j)
    plt.savefig('frecuencias/frecuencia%s.png' % j)
    plt.show()
