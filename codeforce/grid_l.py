import sys
input=sys.stdin.readline
import math

t=int(input().strip())
for _ in range(t):
    n,m=map(int,input().split())
    
    total=n+m*2
    ans=[0,0]
    
    end=math.isqrt(total)+2
    for i in range(1,end):
        if total%(2*i+1)==i:
            if n>=abs(i-(total-i)//(2*i+1)):
                ans=[i,(total-i)//(2*i+1)]
                break
        
    if ans==[0,0]:
        print(-1)
    else:
        print(*ans)