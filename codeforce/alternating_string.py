import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    cnt=0
    for i in range(1,n):
        if s[i]==s[i-1]:
            cnt+=1
            
    print('YES' if cnt<3 else 'NO')