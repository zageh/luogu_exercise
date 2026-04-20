import sys
from bisect import bisect_left

data=sys.stdin.read().split()
n=int(data[0])
a=[int(x) for x in data[1:]]

sum_l=[a[0]]*n

for i in range(1,n):
    sum_l[i]=sum_l[i-1]+a[i]

ans=float('inf')
left_sum=[]    
for k in range(n):
    new_sum=[sum_l[k]-sum_l[i] for i in range(k)]
    new_sum.append(sum_l[k])
    
    left_sum.extend(new_sum)
    left_sum.sort()
    
    for r in range(k+1,n):
        target=sum_l[r]-sum_l[k]
        p=bisect_left(left_sum,target)
        
        if p<len(left_sum):
            ans=min(ans,left_sum[p]-target)
            
        if p>0:
            ans=min(ans,target-left_sum[p-1])
            
    if ans==0:
        print(0)
        sys.exit()
        
print(ans)