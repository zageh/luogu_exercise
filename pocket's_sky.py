import sys
input=sys.stdin.readline

class DSU:
    __slots__=('p','sz')

    def __init__(self,x:int):
        self.p=list(range(x+1))
        self.sz=[1]*(x+1)

    def find(self,x:int):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def union(self,a:int,b:int):
        fa=self.find(a)
        fb=self.find(b)

        if fa==fb:
            return False
        if self.sz[fa]<self.sz[fb]:
            fa,fb=fb,fa
        self.p[fb]=fa
        self.sz[fa]+=self.sz[fb]   
        return True

n,m,k=map(int,input().strip().split())

if k>n:
    print("No Answer")
    sys.exit()

elif n==k:
    print(0)
    sys.exit()

edges=[]
for _ in range(m):
    x,y,l=map(int,input().strip().split())
    edges.append((l,x,y))

edges.sort()

dsu=DSU(n)
cnt=0
ans=0

for v,s,e in edges:
    if dsu.union(s,e):
        ans+=v
        cnt+=1
        if cnt==n-k:
            break

print(ans if cnt==n-k else "No Answer")