import sys
input=sys.stdin.readline

n,m=map(int,input().split())
r=list(map(int,input().split()))
lst=[]
used=[0]*(n+1) 
for _ in range(m):
    d,s,t=map(int,input().split())
    lst.append((d,s,t))

for i,(d,s,t) in enumerate(lst):  # Fixed: Added parentheses around (d,s,t)
    for x in range(s-1,t):
        used[x]+=d
        if used[x]>r[x]:
            print(-1)
            print(i+1)
            exit()

print(0)
