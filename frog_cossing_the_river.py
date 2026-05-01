import sys

data=sys.stdin.read().split()

n=int(data[0])
x=int(data[1])
h=[int(x) for x in data[2:]]

pre=[0]*(n+1)
for i in range(1,n):
    pre[i]=h[i-1]+pre[i-1]

def check(length):
    for i in range(n+1-length):
        if pre[i+length]-pre[i]:
            return False
        
    return True

l,r=0,n
while l<r:
    mid=(l+r)>>1
    
    if check(mid):
        r=mid
        
    else:
        l=mid+1
        
print(r)