import sys
input=sys.stdin.readline

def time(a):
    s=sum(a)
    best=s//2
    bits=1

    for x in a:
        bits|=bits<<x

    for i in range(best,-1,-1):
        if (bits>>i)&1:
            return s-i
    return s

s1,s2,s3,s4=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))

sum_up=time(a)+time(b)+time(c)+time(d)

#这个位运算有点nb