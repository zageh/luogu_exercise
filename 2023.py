import sys
sys.setrecursionlimit(2000)

# def c(x:int,y:int)->int:
#     if y<0 or y>x:
#         return 0
#     ret=1
#     for i in range(y):
#         ret=ret*(x-i)//(i+1)
#     return ret 常用取组合数
    
mod=998244353
n,m=map(int,input().split())
space=n-4*m

ans=0
mm=space//4

#预处理做法
fac=[1]*(n+1)
for i in range(1,n+1):
    fac[i]=fac[i-1]*i%mod
    
ifac=[1]*(n+1)
ifac[-1]=pow(fac[n],mod-2,mod)
for i in range(n,0,-1):
    ifac[i-1]=ifac[i]*i%mod
    
def c(n:int,k:int):
    if k>n or k<0:
        return 0
    return fac[n]*ifac[k]%mod*ifac[n-k]%mod

for i in range(mm+1):
    j=m+i
    sspace=space-4*i
    
    if sspace<0:
        break
    
    aa=c(m+space-3*i,j)
    bb=pow(10,sspace,mod)
    cc=c(j,m)
    term=(((aa*bb)%mod)*cc)%mod
    
    if i%2==1:
        ans=(ans-term+mod)%mod
    else:
        ans=(ans+term)%mod
        
print(ans)