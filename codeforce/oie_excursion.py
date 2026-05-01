import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,m=map(int,input().split())
    p=list(map(int,input().split()))
    
    dan=0
    cnt=1
    
    for i in range(1,n):
        if p[i]==p[i-1]:
            cnt+=1
        else:
            dan=max(cnt,dan)
            cnt=1
            
    dan=max(cnt,dan)        
            
    if dan>=m:
        print('NO')
    else:
        print('YES')