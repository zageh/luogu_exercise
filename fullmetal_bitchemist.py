import sys
input = sys.stdin.readline

out = []

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    a = [int(x) for x in s]
    
    pref = 0
    alt = 0
    cnt = [1, 0, 0]
    ans = 0
    
    for i in range(n):
        if not a[i]:
            pref = (pref + 1) % 3
        else:
            pref = (pref + 2) % 3
            
        if i > 0 and s[i] != s[i - 1]:
            alt += 1
        else:
            alt = 1
            
        good = (i + 1) - cnt[pref]
        cnt[pref] += 1
        
        bad = (alt - 1) >> 1
        
        ans += good - bad
        
    out.append(str(ans)) 
    
sys.stdout.write('\n'.join(out))