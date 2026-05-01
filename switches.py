import sys

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])

ans=[0]*(n<<2)
tag=[0]*(n<<2)

def ls(x:int):
    return x<<1
def rs(x):
    return x<<1|1

def f(p,l,r,k):
    if k:
        tag[p]^=1
        ans[p]=r-l+1-ans[p]
        
def push_up(p):
    ans[p]=ans[ls(p)]+ans[rs(p)]
    
def push_down(p,l,r):
    mid=(l+r)>>1
    
    f(ls(p),l,mid,tag[p])
    f(rs(p),mid+1,r,tag[p])
    tag[p]=0
    
def update(p,tl,tr,l,r,k):
    if tl<=l and tr>=r:
        f(p,l,r,k)
        return
    
    mid=(l+r)>>1
    
    push_down(p,l,r)
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

idx=2
for _ in range(m):
    c=int(data[idx])
    a=int(data[idx+1])
    b=int(data[idx+2])
    
    idx+=3
    
    if c==0:
        update(1,a,b,1,n,1)
        
    if c==1:
        print(query(1,a,b,1,n))