import sys
input=sys.stdin.readline

high=[0]*10005
ans=[]
for line in sys.stdin:
    line=line.strip()
    
    if not line:
        break
    
    l,h,r=map(int,line.split())
    for i in range(l,r):
        high[i]=max(high[i],h)

for i in range(1,10005):
    if high[i]!=high[i-1]:
        ans.append(i)
        ans.append(high[i])

print(*ans)