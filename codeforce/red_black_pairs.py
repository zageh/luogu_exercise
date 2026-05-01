import sys
input=sys.stdin.readline

def com(i,dp):
    cand1,cand2=dp[i-1],10**8
    if fir[i]==sec[i]:
        pass
    else:
        cand1=dp[i-1]+1
        
    if i>=2:
        if (fir[i-1]==sec[i-1] and fir[i]==sec[i]) or (fir[i-1]==fir[i] and sec[i-1]==sec[i]):
            cand2=dp[i-2]
        elif fir[i]!=fir[i-1] and fir[i]!=sec[i] and sec[i-1]!=fir[i-1] and sec[i]!=sec[i-1]:
            cand2=dp[i-2]+2
        else:
            cand2=dp[i-2]+1
            
    dp[i]=min(cand1,cand2)

t=int(input())
for _ in range(t):
    n=int(input())
    fir=input().strip()
    sec=input().strip()
    
    dp=[0]*(n+1)
    if fir[0]==sec[0]:
        pass
    else:
        dp[0]=1
        
    if n==1:
        print(dp[0])
        continue
    
    if (fir[0]==sec[0] and fir[1]==sec[1]) or (fir[0]==fir[1] and sec[0]==sec[1]):
        dp[1]=0
    elif fir[1]!=fir[0] and fir[1]!=sec[1] and sec[0]!=fir[0] and sec[1]!=sec[0]:
        dp[1]=2
    else:
        dp[1]=1
        
    if n==2:
        print(dp[1])
        continue
    
    for i in range(2,n):
        com(i,dp)
        
    print(dp[n-1])