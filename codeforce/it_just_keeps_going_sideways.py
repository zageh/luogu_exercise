import sys
input=sys.stdin.readline
from collections import Counter

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    mn=a[-1]
    cnt=Counter()
    
    b=a.copy()
    b.sort()
    
    pa={}
    pb={}
    for i in range(n):
        if b[i] not in pb:
            pb[b[i]]=[]
        if a[i] not in pa:
            pa[a[i]]=[]
            
        cnt[a[i]]+=1
        pa[a[i]].append(i)
        pb[b[i]].append(i)
        
    moved=max(cnt.values())-1
    
    s=set(b)
    
    for num in s:
        while pa[num] and pb[num]:
            moved+=pb[num].pop()-pa[num].pop()
            
    print(moved)