import sys
from functools import cmp_to_key
input = sys.stdin.readline

n=int(input().strip())
a=input().split()

def com(x:int,y:int):
    if x+y>y+x:
        return -1
    elif x+y<y+x:
        return 1
    else:
        return 0
        
a.sort(key=cmp_to_key(com))

print(''.join(a))