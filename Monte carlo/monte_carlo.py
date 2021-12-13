
import random
 
def monteCarlo(n=1000):
    k = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2 <= 1):
            k = k + 1
    return (4 * float(k) / n)
 
print (monteCarlo())