import sys
input=sys.stdin.readline

t=int(input().strip())
move=(1,2)
for _ in range(t):
    x,y=map(int,input().split())
    if y*2>x:
        print('NO')
        continue
    elif x<-4*y:
        print('NO')
        continue
    c=x-2*y
    
    if c%3!=0:
        print('NO')
        continue
    else:
        print('YES')