import random as r
import collections
import matplotlib.pyplot as plt

N = 100
A = []
B = []
sumatoria = []

for i in range(N):
    a = r.randint(1, 6)
    A.append(a)
    b = r.randint(1, 6)
    B.append(b)
    sumatoria.append(a+b)
counter = collections.Counter(sumatoria)
plt.bar(counter.keys(), counter.values())
plt.title('Frecuencia 100')
plt.savefig('Frecuencia-100.png')
plt.show()

N2 = 1000
A2 = []
B2 = []
sumatoria2 = []

for i in range(N2):
    a2 = r.randint(1, 6)
    A2.append(a2)
    b2 = r.randint(1, 6)
    B2.append(b2)
    sumatoria2.append(a2+b2)
counter2 = collections.Counter(sumatoria2)
plt.bar(counter2.keys(), counter2.values())
plt.title('Frecuencia 1000')
plt.savefig('Frecuencia-1000.png')
plt.show()


N3 = 10000
A3 = []
B3 = []
sumatoria3 = []

for i in range(N3):
    a3 = r.randint(1, 6)
    A3.append(a3)
    b3 = r.randint(1, 6)
    B3.append(b3)
    sumatoria3.append(a3+b3)
counter3 = collections.Counter(sumatoria3)
plt.bar(counter3.keys(), counter3.values())
plt.title('Frecuencia-10000')
plt.savefig('Frecuencia-10000.png')
plt.show()

N4 = 100000
A4 = []
B4 = []
sumatoria4 = []

for i in range(N4):
    a4 = r.randint(1, 6)
    A4.append(a4)
    b4 = r.randint(1, 6)
    B4.append(b4)
    sumatoria4.append(a4+b4)
counter4 = collections.Counter(sumatoria4)
plt.bar(counter4.keys(), counter4.values())
plt.title('Frecuencia-100000')
plt.savefig('Frecuencia-100000.png')
plt.show()
