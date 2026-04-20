import sys

data=sys.stdin.read().split()

n=int(data[0])

cnt=[0]*7
for x in data[1:]:
    c=0
    for d in x:
        if d=='6':
            c+=1
    if c>=6:
        cnt[6]+=1
    else:
        cnt[c]+=1
        
ans=0
ans+=cnt[6]

ans+=min(cnt[5],cnt[1])

if cnt[5]:
    for i in range(1,5):
        if cnt[i]<cnt[5]:
            cnt[5]-=cnt[i]
            ans+=cnt[i]
            cnt[i]=0
        else:
            cnt[i]-=cnt[5]
            ans+=cnt[5]
            cnt[5]=0
            break
        
if cnt[4]:
    if cnt[1]>=2:
        ch=min(cnt[4],cnt[1]//2)
        cnt[1]-=2*ch
        cnt[4]-=ch
        ans+=ch
    if cnt[4]:
           for i in range(2,4):
                if cnt[i]<cnt[4]:
                    cnt[4]-=cnt[i]
                    ans+=cnt[i]
                    cnt[i]=0
                else:
                    cnt[i]-=cnt[4]
                    ans+=cnt[4]
                    cnt[4]=0
                    break
                
if cnt[3]:
    if cnt[2] and cnt[1]:
        ch=min(cnt[3],cnt[2],cnt[1])
        cnt[1]-=ch
        cnt[2]-=ch
        cnt[3]-=ch
        ans+=ch
    if cnt[1]>=3 and cnt[3]:
        ch=min(cnt[3],cnt[1]//3)
        cnt[1]-=3*ch
        cnt[3]-=ch
        ans+=ch
    if cnt[2]>=2 and cnt[3]:
        ch=min(cnt[3],cnt[2]//2)
        cnt[2]-=2*ch
        cnt[3]-=ch
        ans+=ch
    if cnt[3]:
        ans+=cnt[3]//2
        cnt[3]//=2
        
if cnt[2]>=3:
    ans+=cnt[2]//3      
        
print(ans)