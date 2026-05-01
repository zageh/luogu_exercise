import sys
input=sys.stdin.readline


t=int(input().strip())
for _ in range(t):
    n,k,p,m=map(int,input().split())
    a=list(map(int,input().split()))
    
    cost=0
    ans=0
    while True:
        if p<=k:
            x=a[p-1]
            if cost+x>m:
                break
            
            ans+=1
            cost+=x
            a.append(a.pop(p-1))
            p=n
            
        else:
            tmp=a[:k]
            mn=min(tmp)
            
            if cost+mn>m:
                break
            
            i=tmp.index(mn)
            a.append(a.pop(i))
            cost+=mn
            p-=1
            
    print(ans)