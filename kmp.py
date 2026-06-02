import sys

data = sys.stdin.read().split()

a = ' ' + data[0].strip()
b = ' ' + data[1].strip()

la = len(a) - 1
lb = len(b) - 1

j = 0
kmp = [0] * (lb + 1)

for i in range(2, lb + 1):
    while j and b[i] != b[j + 1]:
        j = kmp[j]
        
    if b[i] == b[j + 1]:
        j += 1
        
    kmp[i] = j
    
j = 0

for i in range(1, la + 1):
    while j and b[j + 1] != a[i]:
        j = kmp[j]
        
    if b[j + 1] == a[i]:
        j += 1
        
    if j == lb:
        print(i - lb + 1)
        j = kmp[j]
        
print(*kmp[1:])
        