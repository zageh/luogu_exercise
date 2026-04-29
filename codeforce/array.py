import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=[0]+list(map(int,input().strip().split()))
    
    lst=[[0,0] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if a[i]<a[j]:
                lst[i][1]+=1
            elif a[i]>a[j]:
                lst[i][0]+=1
            else:
                pass
     
    ans=[]       
    for i in range(1,n+1):
        ans.append(max(lst[i][0], lst[i][1]))
        
    print(*ans)