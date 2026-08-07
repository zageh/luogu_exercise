import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    d = []
    c = []
    
    x = 0
    pre = -1
    for b in a:
        if b == pre:
            x += 1
            
        else:
            d.append(x)
            x = 0
            pre = b
            c.append(b)
            
    d.append(x)
            
    d = d[1:]
    
    ori = len(d)
    
    if d.count(0) == ori:
        print(ori)
        continue
    
    else:
        ok = 0
        for i in range(1, ori):
            if d[i] * d[i - 1] > 0:
                print( ori + 2)
                ok = 1
                break
            
        if not ok:
            add = 0

            for i in range(ori):
                if d[i] == 0:
                    continue

                if i > 0 and (i < 2 or c[i] != c[i - 2]):
                    add = 1
                    break

                if i + 1 < ori and (i + 2 >= ori or c[i] != c[i + 2]):
                    add = 1
                    break

            print(ori + add)