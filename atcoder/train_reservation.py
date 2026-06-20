a, b =map(str, input().split())
n = int(a)
x = ord(b) - ord('A')
ok = False
for i in range(n):
    s = input().strip()
    if s[x] == 'o':
        ok = True
        
print("Yes" if ok else "No")