import sys
data=sys.stdin.read().split()
import heapq

n=int(data[0])
k=int(data[1])
a=[int(x) for x in data[2:]]

d={}
for x in a:
    if x not in d:
        d[x]=0
        
    d[x]+=x
    
vals=list(d.values())

vals.sort(reverse=True)

ans=sum(vals[k:])

print(ans)