import sys
input=sys.stdin.readline

def cal(a,b,m):
    aa=a+a
    bb=b+b

    ans=0
    for i in range(m):
        for j in range(m):
            k=0
            while k<m and aa[i+k]==bb[j+k]:
                k+=1
            ans=max(k,ans)
    return ans

class DSU:
    __slots__=('p','sz')
    def __init__(self,n:int):
        self.p=list(range(n+1))
        self.sz=[1]*(n+1)

    def find(self,x:int):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

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
lst=[]
for _ in range(n):
    s=input().strip()
    lst.append(s)

edges=[]
for i in range(n):
    for j in range(i+1,n):
        edges.append((cal(lst[i],lst[j],m),i,j))

edges.sort(reverse=True)

dsu=DSU(n)
ans=0
cnt=0

for v,s,e in edges:
    if dsu.union(s,e):
        ans+=v
        cnt+=1
        if cnt==n-1:
            break

print(ans) 