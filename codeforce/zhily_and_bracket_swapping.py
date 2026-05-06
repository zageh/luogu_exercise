import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    
    ab = 0
    bb = 0
    ca = 0
    cb = 0
    
    ans = ''
    for i in range(n):
        if a[i] == '(':
            ab += 1
        else:
            ab -=1
            
        if b[i] == '(':
            bb += 1
        else:
            bb -=1
            
        if a[i] != b[i]:
            if a[i] == '(':
                cb += 1
            else:
                ca += 1
                
        if ab < 0:
            if bb < 2 or ca == 0:
                ans = 'NO'
                break
            ca -= 1
            bb -= 2
            ab += 2
            
        if bb < 0:
            if ab < 2 or cb == 0:
                ans = 'NO'
                break
            cb -= 1
            ab -= 2
            bb += 2
            
    if ans:
        print(ans)
        continue
    
    print("YES" if ab == 0 and bb == 0 else "NO")