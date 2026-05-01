import math

l,r=map(int,input().split())

end=math.isqrt(r)+1

p=[True]*(end+1)
p[0]=p[1]=False
ps=[]

for i in range(2,end+1):
    if p[i]:
        j=i*i
        ps.append(i)
        while j<=end:
            p[j]=False
            j+=i

is_prime=[True]*(r-l+1)
for pr in ps:
    start=max(pr*pr,(l+pr-1)//pr*pr)

    cur=start
    while cur<=r:
        is_prime[cur-l]=False
        cur+=pr

if l==1:
    is_prime[0]=False

cnt=0
for i in range(l,r+1):
    if is_prime[i-l]:
        cnt+=1

print(cnt)