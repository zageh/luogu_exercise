import sys
input = sys.stdin.readline

out = []

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b = input().strip()
    
    balance = 0
    mn = 0
    cut = 0
    
    for i in range(n):
        if b[i] == '(':
            balance += 1
            
        else:
            balance -= 1
            
            if balance < mn:
                cut = i + 1
                mn = balance
                
    ans = ['0'] * n
    
    for i in range(cut):
        if k == 0:
            break
        
        if b[i] == '(':
            k -= 1
            ans[i] = '1'
            
    for i in range(cut, n):
        if k == 0:
            break
        
        if b[i] == ')':
            k -= 1
            ans[i] = '1'
            
    out.append(''.join(ans))
    
sys.stdout.write('\n'.join(out))