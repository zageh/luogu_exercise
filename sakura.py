import sys
input=sys.stdin.readline

s,e,ns=map(str,input().split())

sh,sm,eh,em=0,0,0,0
ps,pe=False,False

for x in s:
    if x==':':
        ps=True
        continue
    
    if not ps:
        sh=sh*10+int(x)
    else:
        sm=sm*10+int(x)
        
for x in e:
    if x==':':
        pe=True
        continue
    
    if not pe:
        eh=eh*10+int(x)
    else:
        em=em*10+int(x)
   
n=int(ns)
t=(eh-sh)*60+(em-sm)
dp=[0]*(t+1)

for i in range(n):
    x,y,z=map(int,input().split())
    
    if z==0:
        for j in range(x,t+1):
            dp[j]=max(dp[j-x]+y,dp[j])
            
    else:
        k=1
        while k<=z:
            for j in range(t,x*k-1,-1):
                dp[j]=max(dp[j],dp[j-x*k]+y*k)
                
            z-=k
            k<<=1
            
        if z:
            for j in range(t,x*k-1,-1):
                dp[j]=max(dp[j],dp[j-x*z]+y*z)
                
print(dp[t])