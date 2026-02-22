import sys
input=sys.stdin.readline

class DSU:
    __slots__=("p","sz")
    def __init__(self,n:int):
        self.p=list(range(n+1))
        self.sz=[1]*(n+1)

    def find(self,x:int)->int:
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x

    def union(self,a:int,b:int)->bool:
        fa=self.find(a)
        fb=self.find(b)
        if fa==fb:
            return False
        if self.sz[fa]<self.sz[fb]:
            fa,fb=fb,fa
        self.p[fb]=fa
        self.sz[fa]+=self.sz[fb]
        return True

n,m=map(int,input().split())
edges=[]
total=0
count=0
dsu=DSU(n)
for _ in range(m):
    x,y,z=map(int,input().split())
    edges.append((z,x,y))

edges.sort()

for w,s,e in edges:
    if dsu.union(s,e):
        total+=w
        count+=1
        if count==n-1:
            break

if count==n-1:
    print(total)
else:
    print("orz")