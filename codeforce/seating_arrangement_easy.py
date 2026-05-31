import sys
input = sys.stdin.readline

t = int(input().strip())
out = []
for _ in range(t):
    n, x, s = map(int,input().strip().split())
    arr = input().strip()
    arr = arr.lstrip('E')
    
    n = len(arr)
    
    dp = [-1] * (x + 1)
    dp[0] = 0
    
    for i in range(n):
        pd = dp[:]
        
        if arr[i] == 'I':
            for j in range(x - 1, -1, -1):
                if dp[j] < 0:
                    continue
                
                pd[j + 1] = max(dp[j] + 1, pd[j + 1])
                
        elif arr[i] == 'A':
            for j in range(x):
                if dp[j] < 0:
                    continue
                if dp[j] < j * s:
                    pd[j] = max(dp[j] + 1, pd[j])
                pd[j + 1] = max(dp[j] + 1, pd[j + 1])
                    
            if 0 <= pd[x] < x * s:
                pd[x] = max(dp[x] + 1, pd[x])
                
        else:
            for j in range(1, x + 1):
                if dp[j] < 0:
                    continue
                
                if dp[j] < j * s:
                    pd[j] += 1
                    
        dp = pd
                    
    ans = max(dp)
    
    out.append(str(ans))
    
sys.stdout.write('\n'.join(out))