import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

n=int(input().strip())
ds=2*n+1
d1=[False]*ds
d2=[False]*ds
x=[False]*(n+1)
chess=[0]*(n+1)
ans=[]
cnt=0

def dfs(i:int):
    global cnt
    if i==n+1:
        cnt+=1
        if len(ans)<3:
            ans.append(chess[1:].copy())
        return
        
    for j in range(1,n+1):
        if not d1[i-j+n] and x[j]==False and d2[i+j]==False:
            d1[i-j+n]=True
            x[j]=True
            d2[j+i]=True
            chess[i]=j
            dfs(i+1)
            d1[i-j+n]=False
            x[j]=False
            d2[j+i]=False

dfs(1)
for s in ans:
    print(" ".join(map(str,s)))
print(cnt)