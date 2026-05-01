import sys
input=sys.stdin.readline

n=int(input().strip())
m=[]
for _ in range(n):
    row=list(input().strip())
    m.append(row)

word=['y','i','z','h','o','n','g','_','_']

mx=(1,1,1,-1,-1,-1,0,0)
my=(1,-1,0,1,-1,0,1,-1)
is_word=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if m[i][j]=='y':
            for d in range(8):
                stop=False
                nx,ny=i+mx[d],j+my[d]
                if 0<=nx<n and 0<=ny<n and m[nx][ny]=='i':
                    path=[]
                    path.append((i,j))
                    path.append((nx,ny))
                    idx=1
                    while idx<6:
                        cx,cy=nx,ny
                        nx,ny=cx+mx[d],cy+my[d]
                        if 0<=nx<n and 0<=ny<n:
                            if m[nx][ny]==word[idx+1]:
                                idx+=1
                                path.append((nx,ny))
                            else:
                                stop=True
                                idx=0
                                break
                        else:
                            stop=True
                            break
                            
                    if stop or len(path)!=7:
                        continue
                    for x,y in path:
                        is_word[x][y]=True

for i in range(n):
    for j in range(n):
        if not is_word[i][j]:
            m[i][j]='*'
            
for i in range(n):
    print(''.join(m[i]))