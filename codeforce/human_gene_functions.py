import sys

def get(a:str,b:str,c:bool)->int:
    if a==b:
        return 5
    if c:
        if a=='A':
            return -3
        if a=='C':
            return -4
        if a=='G':
            return -2
        if a=='T':
            return -1

    if a=='A':
        if b=='C' or b=='T':
            return -1
        elif b=='G':
            return -2
        
    if a=='C':
        if b=='A':
            return -1
        elif b=='T':
            return -2
        elif b=='G':
            return -3
        
    if a=='G':
        if b=='A' or b=='T':
            return -2
        if b=='C':
            return -3
        
    else:
        if b=='A':
            return -1
        if b=='C' or b=='G':
            return -2
  
data=sys.stdin.read().split()

n1=int(data[0])
s1=data[1].strip()
n2=int(data[2])
s2=data[3].strip()
    
dp=[[0]*(n2+1) for row in range(n1+1)]
for i in range(1,n1+1):
    dp[i][0]=dp[i-1][0]+get(s1[i-1],' ',True)
for i in range(1,n2+1):
    dp[0][i]=dp[0][i-1]+get(s2[i-1],' ',True)

for r1 in range(1,n1+1):
    for r2 in range(1,n2+1):
        dp[r1][r2]=max(dp[r1-1][r2-1]+get(s1[r1-1],s2[r2-1],False),dp[r1-1][r2]+get(s1[r1-1],'g',True),dp[r1][r2-1]+get(s2[r2-1],'f',True))
        
print(dp[n1][n2])        