l, r = map(int, input().split())

x = l ^ r

if not x:
    print(0)
    
else:
    s = bin(x)[2:]
    cur = l
    
    cnt = 1
    out = [l]
    for i in range(len(s)):
        if s[i] == '1':
            cnt += 1
            cur = (1 << (len(s) - i - 1)) ^ cur
            out.append(cur)
            
print(cnt)
print(*out)