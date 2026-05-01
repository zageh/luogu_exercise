import sys
input=sys.stdin.readline

def maxi(s:str):
    ret=list(s)
    n=len(s)
    for i in range(1,n-1):
        if s[i-1]=='1' and s[i+1]=='1':
            ret[i]='1'
    ans=ret.count('1')
    return ans

def mini(s:str):
    ret=list(s)
    n=len(s)
    for i in range(1,n-1):
        if ret[i-1]=='1' and ret[i+1]=='1':
            ret[i]='1'
    for i in range(1,n-1):
        if ret[i-1]=='1' and ret[i+1]=='1':
            ret[i]='0'
    ans=ret.count('1')
    return ans

t=int(input().strip())
answer=[[]for _ in range(t+1)]
for i in range(t):
    n=int(input().strip())
    s=input().strip()
    answer[i].append(mini(s))
    answer[i].append(maxi(s))
    
for i in range(t):  
    print(*answer[i])