import sys
input=sys.stdin.readline

a,b,p=map(int,input().split())
x=pow(a,b,p)
print(f"{a}^{b} mod {p}={x}")