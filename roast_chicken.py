import sys
input=sys.stdin.readline

n=int(input().strip())
plus=n-10

if n<10 or n>30:
    print(0)
    exit()

a=[0]*10
ans=[]
def dfs(pos:int,s:int):
    if pos==10:
        if s==n:
            ans.append(a.copy())
        return

    left=10-pos
    if s+3*left<n:
        return

    if s+left>n:
        return

    for i in range(1,4):
        a[pos]=i
        dfs(pos+1,s+i)

dfs(0,0)
print(len(ans))
for x in ans:
    print(*x)