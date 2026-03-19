import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().strip().split()))
    b=a[::-1]
    
    cnt=0
    while True:
        m=max(b)
        i=b.index(m)
        b=b[i+1:]
        if i==len(b):
            cnt+=1
            break
        a=a[:i]
        cnt+=1
        
    print(cnt)