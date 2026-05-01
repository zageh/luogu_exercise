import sys

data=sys.stdin.read().split()
n=int(data[0])
m=int(data[1])

a=[0]+[int(x) for x in data[2:n+2]]
b=[0]*(n+1)
for i in range(1,n+1):
    b[i]=a[i]-a[i-1]
    
ans=[0]*(n<<2)
tag=[0]*(n<<2)

def ls(p):
    return p<<1
def rs(p):
    return p<<1|1

def push_up(p):
    ans[p]=ans[ls(p)]+ans[rs(p)]

def build (p,l,r):
    tag[p]=0
    
    if l==r:
        ans[p]=b[l]
        return
    
    mid=(l+r)>>1
    build(ls(p),l,mid)
    build(rs(p),mid+1,r)
    
    push_up(p)
    
def f(p,l,r,k):
    tag[p]+=k
    ans[p]+=(r-l+1)*k
    
def push_down(p,l,r):
    mid=(l+r)>>1
    
    if not tag[p]:
        return
    
    f(ls(p),l,mid,tag[p])
    f(rs(p),mid+1,r,tag[p])
    
    tag[p]=0
    
def update(p,tl,tr,l,r,k):
    if tl<=l and tr>=r:
        f(p,l,r,k)
        return 
    
    push_down(p,l,r)
    mid=(l+r)>>1
    if tl<=mid:
        update(ls(p),tl,tr,l,mid,k)
        
    if tr>mid:
        update(rs(p),tl,tr,mid+1,r,k)
        
    push_up(p)
        
def query(p,ql,qr,l,r):
    res=0
    
    if ql<=l and qr>=r:
        return ans[p]
    
    push_down(p,l,r)
    
    mid=(l+r)>>1
    
    if ql<=mid:
        res+=query(ls(p),ql,qr,l,mid)
    if qr>mid:
        res+=query(rs(p),ql,qr,mid+1,r)    
    
    return res

build(1,1,n)

idx=n+2
out=[]
for _ in range(m):
    check=int(data[idx])
    
    if check==1:
        l=int(data[1+idx])
        r=int(data[idx+2])
        k=int(data[idx+3])
        d=int(data[idx+4])
        
        idx+=5
        
        update(1,l,l,1,n,k)
        
        if l+1<=r:
            update(1,l+1,r,1,n,d)
        if r+1<=n:
            update(1,r+1,r+1,1,n,-(k+(r-l)*d))
        
    else:
        p=int(data[idx+1])
        
        idx+=2
        
        out.append(str(query(1,1,p,1,n)))
        
print('\n'.join(out))