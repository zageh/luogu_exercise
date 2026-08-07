import sys
input=sys.stdin.readline

import heapq

t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a=list(map(int,input().split()))
    t = []
    pq = []
    
    for i in range(n):
        row = list(map(int,input().split()))
        t.append(row)
        
    for d in t[-1]:
        heapq.heappush(pq, d)
        
    cost = m

    h = 0
    f = a[-1]
    for d in sorted(pq, reverse=True):
        f -= d
        h += 1
        if f <= 0:
            break
        
    cost = min(cost, h)
    
    for i in range( -2, -n - 1, -1):
        row = t[i]
        mn = pq[0]
        
        for d in row:
            if d > mn:
                heapq.heappush(pq, d)
                
        l = len(pq)
        
        while l > m:
            l -= 1
            heapq.heappop(pq)
            
        h = 0
        f = a[i]
        for d in sorted(pq, reverse=True):
            f -= d
            h += 1
            if f <= 0:
                break
            
        cost = min(cost, h)
        
    print(cost)