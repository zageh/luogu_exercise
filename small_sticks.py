import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    x=int(input().strip())
    if x<=1:
        print(-1)
        continue
    if x==3:
        print(7)
        continue
    if x==4:
        print(4)
        continue
    if x==10:
        print(22)
        continue
    l=x%7
    n=x//7
    if l==0:
        print('8'*n)
        continue
    elif l==1:
        print('10'+'8'*(n-1))
    elif l==2:
        print('1'+'8'*n)
    elif l==3:
        print('200'+'8'*(n-2))
    elif l==4:
        print('20'+'8'*(n-1))
    elif l==5:
        print('2'+'8'*n)
    elif l==6:
        print('6'+'8'*n)