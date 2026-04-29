import sys
input=sys.stdin.readline

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b>0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    cnt=0
    if gcd(a[1],a[0])<a[0]:
        cnt+=1
    if gcd(a[-1],a[-2])<a[-1]:
        cnt+=1
        
    for i in range(1,n-1):
        gcd1=gcd(a[i],a[i-1])
        gcd2=gcd(a[i],a[i+1])
        
        lcm0=lcm(gcd1,gcd2)
        if lcm0<a[i]:
            cnt+=1
    
    print(cnt)