import sys

data = sys.stdin.read().split()

m = int(data[0])
n = int(data[1])
inf = 10 **18

room = []
room.append([0] * (n + 1))

idx = 2
for _ in range(m):
    room.append([0] + [int(x) for x in data[idx: idx + n]])
    idx += n
    
dp = [[[0] * (m + 2) for _ in range(m + 2)] for _ in range(m + n +2)]

dp[1][1][2] = room[1][2] + room[2][1]
dp[1][2][1] = room[1][2] + room[2][1]

for i in range(2, m + n - 1):
    for x1 in range(1, min(i + 1, m) + 1):
        for x2 in range(2, min(i + 1, m) + 1):
            if x1 == x2 and not (x1 == m and i == m + n - 2):
                dp[i][x1][x2] = -inf
                continue
                
            y1, y2 = i - x1 + 2, i - x2 + 2
            
            if y1 > n or y2 >n:
                continue
            
            dp[i][x1][x2] = max(dp[i-1][x1][x2], 
                                dp[i-1][x1-1][x2],
                                dp[i-1][x1-1][x2-1],
                                dp[i-1][x1][x2-1]) + room[x1][y1] + room[x2][y2]
            
print(dp[m+n-2][m][m])