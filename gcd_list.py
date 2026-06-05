import sys
import math

input = sys.stdin.readline
out = []

def check(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return True
        
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    
    if not check(n) or n == 1:
        out.append('1')
        
    else:
        out.append(str(n >> 1))
        
sys.stdout.write('\n'.join(out))