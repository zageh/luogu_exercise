import sys
input=sys.stdin.readline

def gcd(a,b):
    if a<b:
        a,b=b,a
    
    while b:
        a,b=b,a%b
        
    return a

t=int(input().strip())

for _ in range(t):
    n,m,a,b=map(int,input().split())
    
    if gcd(n,a)!=1:
        print('NO')
        continue
    
    if gcd(m,b)!=1:
        print('NO')
        continue
    
    if gcd(m,n)>2:
        print('NO')
        continue
    
    print('YES')