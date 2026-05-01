import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,c,k=map(int,input().strip().split())
    mon=list(map(int,input().strip().split()))
    
    mon.sort()
    
    for m in mon:
        if c>=m and k>0:
            used=min(k,c-m)
            c+=m+used
            k-=used
        elif c>=m:
            c+=m
        else:
            break
        
    print(c)