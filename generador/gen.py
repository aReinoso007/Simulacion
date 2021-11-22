import sys
def gen(n):
    for i in range(n):
        yield i**2

x = [i ** 2 for i in range(1000)]
g = gen(100)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
