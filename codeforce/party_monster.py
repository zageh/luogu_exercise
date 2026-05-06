import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    
    a,b=0,0
    
    for x in s:
        if x=='(':
            a+=1
        elif x==')':
            b+=1
            
    if a==b:
        print('YES')
    else:
        print('NO')