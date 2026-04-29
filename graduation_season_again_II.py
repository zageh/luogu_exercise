import sys
import math
from collections import Counter

data=sys.stdin.read().split()

n=int(data[0])
a=[int(x) for x in data[1:]]

cnt=Counter()

def get(x:int):
    for i in range(1,math.isqrt(x)+1):
        if x%i==0:
            cnt[i]+=1
            if i*i!=x:
                j=x//i
                cnt[j]+=1
            
for x in a:
    get(x)
    
k=[0]*(n+1)
for d,c in cnt.items():
    k[c]=max(k[c],d)
    
for i in range(n-1,0,-1):
    k[i]=max(k[i],k[i+1])
            
for i in range(1,n+1):
    print(k[i])