import sys
input=sys.stdin.readline
from bisect import bisect_left, bisect_right

t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    mid = a[n  // 2]
    
    l = bisect_left(a, mid)
    r = n - bisect_right(a, mid)  
      
    time = max(l, r)
    
    print(time)