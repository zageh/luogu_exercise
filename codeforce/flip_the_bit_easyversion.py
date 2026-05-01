import sys
input=sys.stdin.readline

t=int(input().strip())

for _ in range(t):
    n,k=map(int,input().split())
    b=list(map(int,input().split()))
    p=int(input().strip())-1
    
    left_layer=0
    right_layer=0
    if b[0]!=b[p]:
        left_layer+=1
    if p>0:
        for i in range(p-1,-1,-1):
            if b[i]!=b[i+1]:
                left_layer+=1
                
    if b[-1]!=b[p]:
        right_layer+=1
    if p<n-1:
        for i in range(p+1,n):
            if b[i]!=b[i-1]:
                right_layer+=1
                
    ans=max(right_layer,left_layer)
    
    print(ans)