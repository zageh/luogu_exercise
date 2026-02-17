import sys
input=sys.stdin.readline

t=int(input())
results=[]
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
    b=[]
    for x in a:
        if not b or b[-1]!=x:
            b.append(x)
            
    j=0
    for x in p:
        if j<len(b) and x==b[j]:
            j+=1 
        
    results.append('YES' if j==len(b) else 'NO')
print('\n'.join(results))
        
    