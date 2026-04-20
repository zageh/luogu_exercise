import sys
from collections import Counter

data=sys.stdin.read().split()
n=int(data[0])
c=int(data[1])
a=list(map(int,data[2:]))

cnt=Counter(a)

ans=0
for x in cnt:
    ans+=cnt[x]*cnt.get(x+c,0)

print(ans)