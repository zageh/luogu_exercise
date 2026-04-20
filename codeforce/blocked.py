import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    ok=1
    
    for i in range(1,n):
        if a[i]==a[i-1]:
            print(-1)
            ok=0
            break
    
    if ok:    
        print(*a)