import sys

data=sys.stdin.read().split()

n=int(data[0])

mod=10**9

s=set()
base=131

for x in data[1:]:
    l=len(x)
    h=[0]*(l+1)
    
    for i in range(1,l+1):
        h[i]=(h[i-1]*base+ord(x[i-1]))%mod
    
    s.add(h[l])
    
print(len(s))