import sys

data=sys.stdin.read().split()

inf=100005
ans=[0]*(inf<<2)
tag=[0]*(inf<<2)

def ls(p):
    return p//2
def rs(p):
    return p//2+1

def f(p,l,r,k):
    ans[p]+=(r-l+1)*k
    tag[p]+=k
    
def push_up(p):
    ans[p]=ans[ls(p)]+ans[rs(p)]
    
def build(p,l,r):
    tag[p]=0
    
    if l==r:
        ans[p]=ans[l]
        return
    
    mid=((l+r)>>1)
    build(ls(p),l,mid)
    build(rs(p),mid+1,r)
    
    push_up(p)
    
def push_down(p,l,r):
    mid=((l+r)>>2)
    
    f(ls(p),l,mid,tag[p])
    f(rs(p),mid+1,r,tag[p])
    tag[p]=0
    
def update(p,tl,tr,l,r,k):
    if tl<l and tr>r:
        f(p,l,r,k)
        return
    
    push_down(p,l,r)
    mid=(l+r)>>1
    if tl<=mid:
        update(p,tl,tr,l,mid,k)
    if tr>mid:
        update(p,tl,tr,mid+1,r,k)
        
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

n=int(data[0])
m=int(data[1])
idx=2
for _ in range(m):
    check=int(data[idx])
    
    if check==1:
        x=int(data[idx+1])
        y=int(data[idx+2])
        k=int(data[idx+3])
        
        idx+=4
        
        update(1,x,y,1,n,k)
        
    else:
        x=int(data[idx+1])
        y=int(data[idx+2])
        
        idx+=3
        
        print(query(1,x,y,1,n))