import sys
input=sys.stdin.readline

n=int(input().strip())
ending=0
lst=[]
for _ in range(n):
    s,e=map(int,input().split())
    ending=max(ending,s)
    lst.append((s,e))
cur=0
count=0

lst.sort(key=lambda x:x[1])
while cur<ending:
    for s,e in lst:
        if cur<=s:
            count+=1
            cur=e

print(count)