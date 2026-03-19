import sys
input=sys.stdin.readline

n,p=map(int,input().strip().split())
sum_a=0
lst=[]
l=10**7
for _ in range(n):
    a,b=map(int,input().strip().split())
    lst.append((a,b,b/a))
    l=min(l,b/a)
    sum_a+=a

if sum_a<=p:
    print(-1)
    sys.exit()

def check(x:float):
    charge=p*x
    for a,b,t in lst:
        if t>=x:
            continue
        else:
            charge-=a*x-b
            if charge<0:
                return False
    return True

r=l+1.0
while check(r):
    r*=2

for _ in range(100):
    mid=(l+r)/2.0
    if check(mid):
        l=mid
    else:
        r=mid

print(f"{l:.10f}")