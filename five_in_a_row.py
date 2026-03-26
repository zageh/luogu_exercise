ans=0
a=[0]*26
b=0
w=0

def pd():
    global ans
    if (a[1]+a[2]+a[3]+a[4]+a[5])%5==0:return
    if (a[6]+a[7]+a[8]+a[9]+a[10])%5==0:return
    if (a[11]+a[12]+a[13]+a[14]+a[15])%5==0:return
    if (a[16]+a[17]+a[18]+a[19]+a[20])%5==0:return
    if (a[21]+a[22]+a[23]+a[24]+a[25])%5==0:return
    if (a[1]+a[6]+a[11]+a[16]+a[21])%5==0:return
    if (a[2]+a[7]+a[12]+a[17]+a[22])%5==0:return
    if (a[3]+a[8]+a[13]+a[18]+a[23])%5==0:return
    if (a[4]+a[9]+a[14]+a[19]+a[24])%5==0:return
    if (a[5]+a[10]+a[15]+a[20]+a[25])%5==0:return
    if (a[1]+a[7]+a[13]+a[19]+a[25])%5==0:return
    if (a[5]+a[9]+a[13]+a[17]+a[21])%5==0:return
    ans+=1
    
def dfs(k:int):
    global b,w
      
    if k==26:
        pd()
        return
    
    if b<12:
        b+=1
        a[k]=1
        dfs(k+1)
        b-=1
        
    if w<13:
        w+=1
        a[k]=0
        dfs(k+1)
        w-=1
        
dfs(1)

print(ans)