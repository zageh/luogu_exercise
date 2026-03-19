import sys
input=sys.stdin.readline

def gcd(x:int,y:int):
        while y:
            x,y=y,x%y
        return x
    
def lcm(x:int,y:int):
    return x*y//gcd(x,y)

t=int(input().strip())
for _ in range(t):
    a,b,c,m=map(int,input().strip().split())
    
    ab=lcm(a,b)
    ac=lcm(a,c)
    bc=lcm(b,c)
    abc=lcm(ab,c)
    
    cnta=m//a*6-m//ab*3-m//ac*3+m//abc*2
    cntb=m//b*6-m//ab*3-m//bc*3+m//abc*2
    cntc=m//c*6-m//ac*3-m//bc*3+m//abc*2
    
    print(cnta,cntb,cntc)