import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    
    count=0
    seen=[]
    for v in a:
        while seen and seen[-1]>=v:
            seen.pop()
        if (v-1) in seen:
            seen.append(v)
        else:
            count+=1
            seen=[v]
            
    print(count)