import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=[]
    cnt={}
    for i in range(n):
        x=list(map(int,input().split()))
        a.append(x)
        for s in x:
            cnt[s]=cnt.get(s,0)+1
    m=0
            
    ma=max(cnt.values())
    if ma<=(n-1)*n:
        print('YES')
        continue
    else:
        print('NO')
        continue