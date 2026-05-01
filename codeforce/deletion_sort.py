import sys
input=sys.stdin.readline

def up(a)->bool:
    n=len(a)
    j=True
    for i in range(1,n):
        if a[i]<a[i-1]:
            j=False
    return j
        
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    if up(a):
        print(n)
    else:
        print(1)