import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    ans=1
    
    idx=0
    pos=[-1]*n
    
    s=set()
    l,r=-1,-1
    for i in range(2*n):
        if pos[a[i]]>=idx:
            if not s:
                l,r=i-1,i
                if i>=2 and a[i]==a[i-2]:
                    s.add(a[i-1])
                    l-=1
            if a[i]==a[l+r-i]:
                s.add(a[i])
            else:
                if s:
                    j=0
                    while j in s:
                        j+=1
                    ans=max(ans,j)     
                    s.clear()
                    idx=i
                    continue
            
        else:
            if pos[a[i]]==-1:
                pos[a[i]]=i
                
            if s:
                j=0
                while j in s:
                    j+=1
                ans=max(ans,j)     
                s.clear()
                idx=i
                continue

            if pos[a[i]]!=-1:
                continue
            
    if s:
        j=0
        while j in s:
            j+=1
        ans=max(ans,j)
            
    print(ans)