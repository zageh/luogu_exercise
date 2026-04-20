import sys
input=sys.stdin.readline

t=int(input().strip())

for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    
    if sum(a)%2==1 or n*k%2==0:
        print('YES')
        continue
    
    print('NO')