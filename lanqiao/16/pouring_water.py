import os
import sys

input=sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))

def check(x:int):
  for i in range(k):
      more=0
      for j in range(i,n,k):
        more+=a[j]-x
        if more<0:
          return False
  return True

l,r=0,sum(a)//n
while l<r:
  mid=(l+r+1)//2
  if check(mid):
    l=mid
  else:
    r=mid-1
  
print(l)