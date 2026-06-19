import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mn = 100000
    
    for i in range(n):
        if a[i] < mn:
            mn = a[i]
        else:
            a[i] = mn
            
    print(sum(a))