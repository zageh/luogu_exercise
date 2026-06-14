s = input().strip()

ans = ''

for x in s:
    if ord('0') <= ord(x) <= ord('9'):
        ans += x
        
print(ans)