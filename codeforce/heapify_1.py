import sys
input=sys.stdin.readline

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=[0]+list(map(int,input().split()))
    judge=True
    
    for i in range(1,n+1):
        if i%2==0:
            continue
        pos=[]
        x=i
        while(x<=n):
            pos.append(x)
            x*=2
            
        comparison=[a[p] for p in pos]
        if sorted(comparison)!=sorted(pos):
            judge=False
    print('YES' if judge else 'NO')