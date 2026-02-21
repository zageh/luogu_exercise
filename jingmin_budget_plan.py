import sys
input=sys.stdin.readline

n,m=map(int,input().split())
main=[None]*(m+1)
vice=[[] for _ in range(m+1)]

for i in range(m):
    v,e,type1=map(int,input().split())
    if type1==0:
        main[i+1]=(v,e)
    else:
        vice[type1].append((v,e))

ex=[0]*(n+1)

for i in range(1,m+1):
    if main[i] is None:
        continue

    v0,e0=main[i]
    combo=[]
    combo.append((v0,e0*v0))

    if len(vice[i])>=1:
        v1,e1=vice[i][0]
        combo.append((v0+v1,e0*v0+e1*v1))
    if len(vice[i])>=2:
        v2,e2=vice[i][1]
        combo.append((v0+v2,e0*v0+e2*v2))
        combo.append((v0+v1+v2,e0*v0+e1*v1+e2*v2))

    for j in range(n,0,-1):
        best=ex[j]
        for give,get in combo:
            if j>=give:
                cand=ex[j-give]+get
                if cand>best:
                    best=cand
        ex[j]=best

print(ex[n])