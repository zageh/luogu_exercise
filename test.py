n=int(input())
lines=2*n-2
lst=[[],[],['-','-'],[]]
for _ in range(0,n):
    lst[0].append('o')
    lst[1].append('*')

i=1
while len(lst[0])>3:
    print(''.join(lst[0]+lst[1]+lst[2]+lst[3]))
    if i%2==1:
        lst[3].append('o')
        lst[3].append('*')
        lst[1].pop()
        lst[0].pop()
    tmp=lst[2]
    lst[2]=lst[1]
    lst[1]=tmp
    i+=1

lst[0]=['o']
lst[1]=['-','-']
lst[2]=['*','o','*','*','o']
print(''.join(lst[0]+lst[1]+lst[2]+lst[3]))
lst[1].append('*')
lst[1].append('o')
lst[1].append('*')
lst[1].append('o')
lst[1].append('*')
lst[2].clear()
print(''.join(lst[0]+lst[1]+lst[2]+lst[3]))
lst[2]=['o']
lst[0].clear()
print(''.join(lst[0]+lst[1]+lst[2]+lst[3]))