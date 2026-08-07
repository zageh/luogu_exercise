import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a=list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = x - 1
    j = y - 1

    ca = 0
    cb = 0
    cnt = 0
    ans = 0

    while cnt < n + m - 1 and (i >= 0 or j >= 0):
        if j < 0 or (i >= 0 and a[i] > b[j]):
            if ca < n:
                ans += a[i]
                ca += 1
                cnt += 1
            i -= 1

        elif i < 0 or b[j] > a[i]:
            if cb < m:
                ans += b[j]
                cb += 1
                cnt += 1
            j -= 1

        else:
            ans += a[i]
            cnt += 1
            i -= 1
            j -= 1

    print(ans)