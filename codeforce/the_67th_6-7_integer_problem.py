import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    a=list(map(int,input().split()))
    print(2*max(a)-sum(a))