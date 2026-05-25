import sys
input = sys.stdin.readline

n, k = map(int, input().split())

mod = 10000

cnt = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    cnt[i][0] = 1
    
for i in range(1, n + 1):
    for j in range(1, k + 1):
        
        cnt[i][j] = cnt[i - 1][j] + cnt[i][j - 1]
        
        if j >= i:
            cnt[i][j] -= cnt[i - 1][j - i]
            
        cnt[i][j] %= mod
            
print(cnt[n][k])