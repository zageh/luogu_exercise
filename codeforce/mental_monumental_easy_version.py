import sys
input=sys.stdin.readline
from collections import Counter
import heapq

def check(h,c,p):
    cc=c.copy()
    pq=h.copy()
    
    ok=True
    for i in range(p-1,-1,-1):
        if cc[i]:
            cc[i]-=1
            continue
        
        while pq and cc[-pq[0]]==0:
            heapq.heappop(pq)
        
        if not pq:
            ok=False
            break
        
        x=heapq.heappop(pq)
        x*=-1
        
        if x>2*i:
            cc[x]-=1
            continue
        
        ok=False
        break
            
    return ok

t=int(input().strip())
for _ in range(t):
    n=int(input())
    
    cnt=Counter()
    heap=[]
    
    a=list(map(int,input().split()))
    for x in a:
        cnt[x]+=1
        heap.append(-x)
        
    heapq.heapify(heap)
        
    l,r=0,n
    while l<r:
        mid=(l+r+1)//2
        
        if check(heap,cnt,mid):
            l=mid
        else:
            r=mid-1
            
    print(l)