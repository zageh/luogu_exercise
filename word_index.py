import sys
import math
input=sys.stdin.readline

def get(s:str):
    alphabet_dict={chr(i+97): i+1 for i in range(26)}
    
    n=len(s)
    result=1
    if n>6:
        return 0
    for i in range(n-1):
        if s[i]>=s[i+1]:
            return 0
    
    def combine(x,y):
        if y>x:
            return 0
        return math.comb(x,y)
    for l in range(1,n):
        result+=combine(26,l)
    last=0
    for i in range(n):
        char=s[i]
        v=alphabet_dict[char]
        
        for j in range(last+1,v):
            result+=combine(26-j,n-i-1)
        last=v
        
    return result
        
s=input().strip()
print(get(s))