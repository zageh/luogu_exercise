import sys
input=sys.stdin.readline

v=int(input())
n=int(input())
lst=[]
for _ in range(n):
    x=int(input())
    lst.append(x)

bits=1
for x in lst:
    bits|=bits<<x

ans=0
for i in range(v,1,-1):
    if (bits>>i)&1:
        ans=v-i
        break

print(ans)