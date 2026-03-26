import sys
input=sys.stdin.readline

n=int(input().strip())
ans=[]

def dfs(i,s,last,c,p):
    if c=='+':
        s+=last
        last=i
        p=str(i)+'+'+p
    elif c=='-':
        s-=last
        last=i
        p=str(i)+'-'+p
    else:
        last=int(str(i)+str(last))
        p=str(i)+' '+p
    if i==1:
        if s+last==0:
            ans.append(p)
        return
    dfs(i-1,s,last,' ',p)
    dfs(i-1,s,last,'+',p)
    dfs(i-1,s,last,'-',p)

dfs(n-1,0,n,' ',str(n))
dfs(n-1,0,n,'+',str(n))
dfs(n-1,0,n,'-',str(n))

ans.sort()
print('\n'.join(ans))