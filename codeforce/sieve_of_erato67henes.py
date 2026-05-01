t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    if any(y == 67 for y in a):
        print('YES')
    else:
        print('NO')