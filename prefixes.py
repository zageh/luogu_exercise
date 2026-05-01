import sys
input=sys.stdin.buffer.readline

mod=(1<<64)-1

t=int(input())
for _ in range(t):
    
    n,m,q=map(int,input().split())
    ans=0
    s=[[0]*(m+1) for x in range(n+1)]
    
    for row in range(1,n+1):
        matrix=[0]+list(map(int,input().split()))
        for i in range(1,m+1):
            s[row][i]=s[row-1][i]+s[row][i-1]-s[row-1][i-1]+matrix[i]
            s[row][i]&=mod

    for i in range(q):
        u,v,x,y=map(int,input().split())
        cnt=(s[x][y]-s[x][v-1]-s[u-1][y]+s[u-1][v-1])
        cnt&=mod
        ans^=cnt
        
    print(ans)