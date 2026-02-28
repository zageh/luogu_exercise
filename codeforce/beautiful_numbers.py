import sys
input=sys.stdin.readline

def f(x):
    s=0
    for i in str(x):
       s+=int(i)
    return s

t=int(input().strip())
for _ in range(t):
    x=int(input().strip())
    xs=str(x)
    xs = str(int(xs[0])-1) + xs[1:]
    lst=[]
    for s in xs:
        lst.append(int(s))
    lst.sort()
    num=f(x)
    count=0
    while num>9:
        count+=1
        num-=lst[-1]
        lst.pop()
        
    print(count)