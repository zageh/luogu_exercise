import sys
input=sys.stdin.readline

n=int(input().strip())


last1=1
last=2
this=0
if n ==1:
    this=last1
elif n==2:
    this=2
else:
    for i in range(2,n):
        this=last1+last
        last1=last
        last=this

ans=this
print(ans)