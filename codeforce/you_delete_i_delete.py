import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    s = input().strip()
    d1 = 0
    d0 = 0
    d = []
    
    for x in s:
        if d1 == 0 and x == '1':
            d1 = 1
            continue
        if d0 == 0 and x == '0':
            d0 = 1
            continue
        
        d.append(x)
        
    sys.stdout.write(''.join(d) + '\n')