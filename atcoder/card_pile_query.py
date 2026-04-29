import sys
sys.setrecursionlimit(10**7)

data=sys.stdin.read().split()

n=int(data[0])
q=int(data[1])

pos=[0]*(n+1)

def find(x:int)->int:
    if pos[x]==x:
        return x
    
    pos[x]=find(pos[x])
    return pos[x]

for i in range(1,n+1):
    pos[i]=i

idx=2
for _ in range(q):
    c=int(data[idx])
    p=int(data[idx+1])
    
    pos[c]=p
    
    idx+=2
    
ans=[0]*(n+1)
for i in range(1,n+1):
    dir=find(i)
    
    ans[dir]+=1
    
print(*ans[1:])