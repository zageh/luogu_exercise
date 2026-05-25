import sys

data = sys.stdin.read().strip().split()

n = int(data[0])
s = data[1]

ans = n * (n + 1) // 2

cnt = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        cnt += 1
        
    else:
        ans -= cnt * (cnt + 1) // 2
        cnt = 1
     
ans -= cnt * (cnt + 1) // 2   
print(ans)