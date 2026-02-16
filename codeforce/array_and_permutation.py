#这题没有ai我根本做不了
import sys
input=sys.stdin.readline

t=int(input())
results=[]
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
    ok=True
    i=0
    k=0
    
    used=[False]*n
    where=[0]*(n+1)
    for idx,v in enumerate(p):
        where[v]=idx
    
    while k<n and i<n:
        while k<n and used[k]:
            k+=1
            
        v=p[k]
        if a[i]!=v:
            k+=1
            continue
        
        start=where[v]
        if used[start]:
            ok=False
            break
        
        j=i
        while j<n and a[j]==v:
            j+=1
        seg_len=j-i
        
        for tpos in range(start,start+seg_len):
            if tpos>=n or used[tpos]:
                ok=False
                break
            used[tpos]=True
            
        if not ok:
            break
            
        i=j
        k+=1
    if i!=n:
        ok=False
        
    results.append('YES' if ok else 'NO')
print('\n'.join(results))
        
    