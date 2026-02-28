import sys
input=sys.stdin.readline

n=int(input().strip())
m1,m2=map(int,input().split())
s=list(map(int,input().split()))

if m1==1:
    print(0)
    sys.exit()

need=[]
x=m1
p=2
while p**2<=x:
    if x%p==0:
        cnt=0
        while x%p==0:
            cnt+=1
            x//=p
        need.append((p,cnt*m2))
    p+=1 if p==2 else 2
if x>1:
    need.append((x,m2))
    
inf=10**30
ans=inf

for si in s:
    t=0
    ok=True
    for p,a in need:
        y=si
        cnt=0
        while y%p==0:
            cnt+=1
            y//=p
        if y==0:
            ok=False
            break
        req=(a+cnt-1)//cnt
        t=max(req,t)
    if ok:
        ans=min(ans,t)

print (-1 if ans==inf else ans)