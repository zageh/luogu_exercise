import sys 
input=sys.stdin.read

data=input().split()
n=int(data[0])
num=[x for x in data[1:]]
    
is_prime=[True]*(10**7+1)
is_prime[0]=False
is_prime[1]=False

for i in range(2,int((10**7)**0.5+1)):
    if is_prime[i]:
        j=i**2
        while j<10**7+1:
            is_prime[j]=False
            j+=i

ans=-1
found=False
def dfs(i,s):
    global ans,found
    if found:
        return

    if i==len(s):
        n=int(''.join(s))
        if is_prime[n]:
            ans=n
            found=True
        return

    if s[i]!='*':
        dfs(i+1,s)
    else:
        if i==len(s)-1:
            if i==0:
                digit=[2,3,5,7]
            else:
                digit=[1,3,7,9]
            for d in digit:
                s[i]=str(d)
                dfs(i+1,s)
                if found:
                    return
        else:
            for d in range(10):
                s[i]=str(d)
                dfs(i+1,s)
                if found:
                    return
        s[i]='*'

for x in num:
    ans=-1
    found=False
    if x[-1]!='*' and (int(x[-1])%2==0 or (x[-1]=='5' and len(x)>1)):
        print(-1)
        continue

    s=list(x)
    dfs(0,s)
    print(ans)