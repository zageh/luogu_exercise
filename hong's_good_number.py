import math
n = int(input())

def isqrt(x):
    r = int(math.sqrt(x))
    
    while (r + 1) * (r + 1) <= x:
        r += 1
        
    while r * r > x:
        r -= 1
        
    return r

for i in range(2, 10 ** 6 + 1):
    if n % i == 0:
        if n % (i * i) == 0:
            print(i, n // (i * i))
            break
        
        else:
            print(isqrt(n // i), i)
            break