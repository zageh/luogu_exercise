n=int(input())
a=list((map(int,input().split())))

a.sort()
ans=[]
for x in a:
    ans.append(x)
print(*ans)