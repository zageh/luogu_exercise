import sys
input = sys.stdin.readline

n = int(input().strip())
d = list(map(int, input().split()))

cnt = d[0]  
for i in range(1, n):
    if d[i] > d[i-1]:
        cnt += d[i] - d[i-1]  

print(cnt)