import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    c0 = 0
    c1 = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            if s[i] == '0':
                c0 += 1
            else:
                c1 += 1

    ans = c0 + c1
    d = c0 - c1

    if abs(d) <= 1:
        print(ans)

    elif d > 1:
        need = d - 1
        a = (s[0] == '1') + (s[-1] == '1')

        print(ans + need if a >= need else -1)

    else:
        need = -d - 1
        a = (s[0] == '0') + (s[-1] == '0')

        print(ans + need if a >= need else -1)