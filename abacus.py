import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
a = [int(x) for x in data[2:]]

a.sort()

print(*a)