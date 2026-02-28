import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if p[0] != n:
        idx = p.index(n)
        p[0], p[idx] = p[idx], p[0]

    print(*p)