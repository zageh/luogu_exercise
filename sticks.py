import sys
sys.setrecursionlimit(3000)
input=sys.stdin.read

data=input().split()
n=int(data[0])
a=[int(x) for x in data[1:] if int(x)<=50]
a.sort(reverse=True)
n=len(a)

if n==0:
    print(0)
    sys.exit()

total=sum(a)
l=max(a)
taken=[False]*n

def dfs(cnt,cur,i,l):
    if cur==n:
        return True

    fail=-1
    for j in range(i,n):
        if not taken[j] and cnt+a[j]<=l and a[j]!=fail:
            taken[j]=True
            if cnt+a[j]==l:
                if dfs(0,cur+1,0,l):
                    return True
                fail=a[j]
                taken[j]=False
                break

            else:
                if dfs(cnt+a[j],cur+1,j+1,l):
                    return True
                fail=a[j]
                taken[j]=False

            if cnt==0:
                break
    return False

ans=total
for d in range(l,total//2+1):
    if total%d!=0:
        continue

    for i in range(n):
        taken[i]=False

    if dfs(0,0,0,d):
        ans=d
        break

print(ans)