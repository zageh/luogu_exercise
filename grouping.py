import heapq
import sys
input=sys.stdin.readline

n=int(input().strip())
a=list(map(int,input().split()))
a.sort()

groups={}
for x in a:
    last=x-1
    if last in groups and groups[last]:
        min_len=heapq.heappop(groups[last])
        if x not in groups:
            groups[x]=[]
        heapq.heappush(groups[x],min_len+1)
    else:
        if x not in groups:
            groups[x]=[]
        heapq.heappush(groups[x],1)

ans=10**5+1
for v in groups.values():
    if v:
        ans=min(ans,v[0])
print(ans)
#今天学到这个，有点厉害