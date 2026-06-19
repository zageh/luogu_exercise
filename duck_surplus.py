import sys
input = sys.stdin.readline

out = []

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    i = 0

    while i < n:
        cur = a[i]
        i += 1

        while i < n and cur >a[i]:
            cur += a[i]
            i += 1

        ans = max(ans, cur)

    out.append(str(ans))

sys.stdout.write('\n'.join(out))