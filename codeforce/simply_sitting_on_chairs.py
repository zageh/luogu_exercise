import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    l=[0]+list(map(int,input().split()))
    
    ans=0
    for i in range(1,n+1):
        if l[i]<=i:
            ans+=1
            
    print(ans)