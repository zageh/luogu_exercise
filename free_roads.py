import sys
sys.setrecursionlimit(2000000)

class DSU:
    __slots__=("p","sz")

    def __init__(self,n):
        self.sz=[1]*(n+1)
        self.p=list(range(n+1))

    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def union(self,a,b):
        fa=self.find(a)
        fb=self.find(b)

        if fa==fb:
            return False

        if self.sz[fa]<self.sz[fb]:
            fa,fb=fb,fa
        self.p[fb]=fa
        self.sz[fa]+=self.sz[fb]
        return True
        
data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
k=int(data[2])

idx=3
road0=[]
road1=[]
while idx<=3*m+1:
    u=int(data[idx])
    v=int(data[idx+1])
    c=int(data[idx+2])
    if c==0:
        road0.append((u,v))
    else:
        road1.append((u,v))
    idx+=3

if len(road0)<k:
    print('no solution')
    sys.exit()

dsu_0=DSU(n)
for s,e in road1:
    dsu_0.union(s,e)
    
must=[]
for s,e in road0:
    if dsu_0.union(s,e):
        must.append((s,e))

if len(must)>k:
    print('no solution')
    sys.exit()
        
dsu=DSU(n)

ans=[]
for s,e in must:
    ans.append((s,e,0))
    dsu.union(s,e)
    
for s,e in road0:
    if dsu.union(s,e):
        ans.append((s,e,0))
    if len(ans)==k:
        break
    
for s,e in road1:
    if dsu.union(s,e):
        ans.append((s,e,1))
    if len(ans)==n-1:
        break
        
if len(ans)==n-1:
    for a,b,c in ans:
        print(a,b,c)
        
else:
    print('no solution')