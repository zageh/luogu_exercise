import sys

data=sys.stdin.read().split()

a=int(data[0])
b=int(data[1])
c=int(data[2])

if a!=b and b==c:
    print("Yes")
else:
    print("No")