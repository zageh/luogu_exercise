import sys

data=sys.stdin.read().split()
n=int(data[0])
a=[int(x) for x in data[1:n+1]]
b=[int(x) for x in data[n+1:]]

a.sort(reverse=True)
b.sort(reverse=True)

cnt=n

i,j=0,0
while i<n and j<n:
    if a[i]>b[j]:
        cnt-=1
        i+=1
        j+=1
    else:
        j+=1

print(cnt)