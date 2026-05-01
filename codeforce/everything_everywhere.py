import sys
input=sys.stdin.readline
import math

t=int(input().strip())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    
    ans=0
    for i in range(n-1):
        if math.gcd(p[i],p[i+1])==abs(p[i]-p[i+1]):
            ans+=1
            
    print(ans)