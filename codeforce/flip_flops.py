import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,c,k=map(int,input().strip().split())
    mon=list(map(int,input().strip().split()))
    
    for m in mon:
        if c>=m+1 and k>0:
            k-=1
            c+=m+1
        elif c>=m:
            c+=m
        else:
            pass
        
    print(c)