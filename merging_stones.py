import sys
data=sys.stdin.read().split()

n=int(data[0])
a=[int(x) for x in data[1:]]
a=a*2
mn=[[0]*(2*n+1) for _ in range(2*n+1)]
mx=[[0]*(2*n+1) for _ in range(2*n+1)]

pref=[0]*(2*n+1)
pref[0]=a[0]
for i in range(1,2*n):
    pref[i]=a[i-1]+pref[i-1]

for length in range(2,n+1):
    for l in range(1,2*n-length+2):
        r=l+length-1
        s=10**9
        b=0
        d=pref[r]-pref[l-1]
        for k in range(l,r):
            s=min(s,mn[l][k]+mn[k+1][r]+d)
            b=max(b,mx[l][k]+mx[k+1][r]+d)
        mx[l][r]=b
        mn[l][r]=s

a_l,a_h=10**9,0
for l in range(1,n+1):
    r=l+n-1
    a_l=min(a_l,mn[l][r])
    a_h=max(a_h,mx[l][r])

print(a_l)
print(a_h)