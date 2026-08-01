import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if (n >> 1) < m:
        print("NO")
        continue
    
    c = []
    s = 0
    ok = True
    
    c.extend((x, 1) for x in a)
    c.extend((x, -1) for x in b)
    
    c.sort()
    
    for _, check in c:
        s += check
        if s < 0:
            ok = False
            break
        
    if ok:
        s = 0
        for _, check in c[::-1]:
            s += check
            if s < 0:
                ok = False
                break
            
    print("YES" if ok else "NO")