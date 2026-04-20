import sys

s=sys.stdin.read().strip()

mx='a'

for x in s:
    if ord(x)>ord(mx):
        mx=x

cnt=0
for x in s:
    if x==mx:
        cnt+=1
        
print(mx*cnt)