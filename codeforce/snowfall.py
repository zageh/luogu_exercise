import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    ans=[]
    els3=[]
    els2=[]
    els=[]
    for x in a:
        if x%6==0:
            ans.append(x)
        else:
            if x%2==0:
                els2.append(x)
            elif x%3==0:
                els3.append(x)
            else:
                els.append(x)
                
    ans=ans+els3+els+els2
    
    print(*ans)