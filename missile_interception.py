import sys
input=sys.stdin.readline
from bisect import bisect_left,bisect_right 

m=list(map(int,input().split()))

d1=[]
for x in m:
    x=-x

    if not d1 or x>=d1[-1]:
        d1.append(x)
    else:
        p=bisect_right(d1,x)
        d1[p]=x

d2=[]
for x in m:
    p=bisect_left(d2,x)
    if p==len(d2):
        d2.append(x)
    else:
        d2[p]=x

print(len(d1))
print(len(d2))