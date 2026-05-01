import sys

data=sys.stdin.read().split()

d=int(data[0])

idx=1
for _ in range(d):
    s2=data[idx]
    s1=data[idx+1]
    idx+=2
    
    l=len(s1)
    if s1[0]!=s2[0] or s1[-1]!=s2[-1]:
        print(-1)
        continue
    
    ok=True
    ans=0
    for i in range(1,l-1):
        if s1[i]!=s2[i]:
            if s1[1]!=s1[i-1] and s1[i-1]==s1[i+1]:
                ans+=1
                continue
            
            else:
                ok=False
                break
    
    if ok:
        print(ans)
    else:
        print(-1)