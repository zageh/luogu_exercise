n = int(input())
if n & 1:
    print(-1)
    exit()
    
ans = ['0'] * (n >> 1) + ['1'] * (n >> 1)
print(''.join(ans))