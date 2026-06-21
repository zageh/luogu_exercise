n,m,k = map(int, input().split())

mn = ((n * m + 1) >> 1 ) + 2 * ((n * m) >> 1)

if n * m == 1:
    print("YES")
    print(k)
    exit()

if k < mn:
    print("NO")
    exit()
    
dp = [[1] * m for _ in range(n)]

d = max(k - ((n * m + 1) >> 1), 1)

f = max(1, (m * n) >> 1)
x = d // f
first = x + d % f

for i in range(n):
    for j in range(m):
        if (i + j) & 1:
            if first:
                dp[i][j] = first
                first = 0
                
            else:
                dp[i][j] = x
                
print('YES')
for i in range(n):
    print(*dp[i])