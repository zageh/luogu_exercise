import sys
input=sys.stdin.readline

n=int(input().strip())
lst=[]
for _ in range(n):
    s,b=map(int,input().strip().split())
    lst.append((s,b))

ans=10**7
def dfs(i:int,sour,bitter,chosen):
    global ans

    if i==n:
        if chosen:
            ans=min(ans,abs(sour-bitter))
        return
    
    dfs(i+1,sour*lst[i][0],bitter+lst[i][1],True)
    
    dfs(i+1,sour,bitter,chosen)

dfs(0,1,0,0)
print(ans)