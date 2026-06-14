import sys
input = sys.stdin.readline

n = int(input())
x = [[] for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    
    for j in a[1:]:
        x[j - 1].append(i + 1)
        
for i in range(n):
    if x[i]:
        print(len(x[i]), *x[i])
        
    else:
        print(0)