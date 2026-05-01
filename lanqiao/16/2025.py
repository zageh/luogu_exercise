import os
import sys

input=sys.stdin.readline

h,w=map(int,input().split())
fill='2025'*200
ans=['']*h
for i in range(h):
  for j in range(w):
    ans[i]+=fill[i+j]

for i in range(h):
  print(ans[i])