import sys

s = sys.stdin.read().strip()
 
c = set(s)

if len(c) != 2:
    print('No')
else:
    print("Yes")