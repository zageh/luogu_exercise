import sys
input=sys.stdin.readline

n=int(input().strip())
a=list(map(int,input().strip().split()))

exist=[False]*(n+1)

for i in range(n):
    if exist[a[i]]==False:
        exist[a[i]]=True
    else:
        while True:
            a[i]+=1
            if exist[a[i]]==False:
                exist[a[i]]=True
                break

print(*a)