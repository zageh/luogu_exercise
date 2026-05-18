import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    
    if a%2==1 and b%2==1:
        print('NO')
    else:
        print('YES')