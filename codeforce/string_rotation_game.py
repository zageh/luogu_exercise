import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    s=input().strip()
    ans=n
    minus=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            minus+=1
    ans=n-minus
    if s[0]!=s[-1] and minus>0:
        ans+=1
    if minus==n-1:
        ans=1
    print(ans)