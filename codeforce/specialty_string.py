import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    s=input().strip()
    ls=[]
    for c in s:
        if ls and ls[-1]==c:
            ls.pop()
        else:
            ls.append(c)
            
    if ls:
        print('NO')
    else:
        print('YES')