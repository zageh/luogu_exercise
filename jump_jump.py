import sys
input=sys.stdin.readline

n=int(input().strip())
h=list(map(int,input().split()))

h.sort()
l,r=0,n-1
index=1
count=h[r]**2
while r>=l:
    count+=(h[r]-h[l])**2
    index+=1
    if index%2==0:
        r-=1
    else:
        l+=1
print(count)