import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,k=map(int,input().strip().split())
    ok=True
    mid=True if k>n//2 else False
    if mid:
        l=n-k
        r=k-1
    
    da={}
    db={}
    
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    for i in range(n):
        da[a[i]]=i
        if b[i]!=-1:
            if b[i] in db:
                ok=False
                break
            db[b[i]]=i
            
    if not ok:
        print("NO")
        continue
    
    for i in range(1,n+1):
        if i in db:
            if mid:
                if not ((l<=db[i]<=r and l<=da[i]<=r) or (db[i]==da[i])):
                    ok=False
                    break
            
            else:
                if da[i]!=db[i]:
                    ok=False
                    break
                
    print("YES" if ok else "NO")