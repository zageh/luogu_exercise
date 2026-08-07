import sys
input=sys.stdin.readline

import math

def check(x):
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
        
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    print("YES" if check(n + 1) else "NO")