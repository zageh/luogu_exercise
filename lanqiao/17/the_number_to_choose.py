import sys
input=sys.stdin.readline
import math

n,k=map(int,input().split())
a=list(map(int,input().split()))

p=a[0]
for i in range(1,n):
    p=p*a[i]//math.gcd(p,a[i])

print(k//math.gcd(p,k))