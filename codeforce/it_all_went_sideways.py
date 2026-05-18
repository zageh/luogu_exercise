import sys
input=sys.stdin.readline
from collections import Counter

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    mn=a[-1]
    moved=0
    cnt=Counter()
    cnt[mn]+=1
    
    for i in range(n-2,-1,-1):
        if mn<a[i]:
            moved+=a[i]-mn
            a[i]=mn
        else:
            mn=a[i]
            
        cnt[a[i]]+=1
    
    moved+=max(cnt.values())-1
    
    print(moved)