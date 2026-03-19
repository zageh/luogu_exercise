import sys
input=sys.stdin.readline

n=int(input().strip())

a=[[1]]
for _ in range(n):
    l=len(a)
    b=[[0]*(2*l) for row in range(2*l)]
    for i in range(l):
        for j in range(l):
            b[i][j+l]=a[i][j]
            b[i+l][j]=a[i][j]
            b[i+l][j+l]=a[i][j]
    a=b

for row in a:
    print(*row)