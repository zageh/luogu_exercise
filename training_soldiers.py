import sys
input=sys.stdin.readline

n,s=map(int,input().split())
sum_l=[0]*1000005
total=0
r=0
for _ in range(n):
    p,c=map(int,input().split())
    r=max(r,c)
    
    sum_l[c]+=p
    
    total+=p*c
    
if total<s:
    print(total)
    sys.exit()
    
for k in range(r-1,-1,-1):
    sum_l[k]+=sum_l[k+1]
    
cur=mn=total

for k in range(1,r+1):
    cur+=s-sum_l[k]
    if mn>cur:
        mn=cur
        
print(mn)