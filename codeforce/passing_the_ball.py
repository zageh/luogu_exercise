import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    ans=0
    s=input().strip()
    for i in range(n):
        ans=i+1
        if s[i]=='L':
            break
        
    print(ans)