import sys
input=sys.stdin.readline

n=int(input().strip())
a=list(map(int,input().strip().split()))
q=int(input().strip())

pos={}
for i,x in enumerate(a,1):
    pos[x]=i

for _ in range(q):
    p=int(input().strip())
    ans=pos.get(p,0)

    print(ans)
