import heapq

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    if n==1:
        print(1)
        continue
    if n==2:
        print(1,2)
        continue

    ans=[]
    behind=0
    if n%2==0:
        behind=n
        n-=1

    i=1
    bit_l=0
    while i<=n:
        i*=2
        bit_l+=1

    num=[[]for _ in range(bit_l+1)]

    for i in range(bit_l):
        for x in range(2**i,min(2**(i+1),n+1)):
            num[i+1].append(x)
     
    for i in range(bit_l):       
        if num[bit_l-i]:
            l=bit_l-i
            if l==1 and num[1]:
                num[1].clear()
                ans.append(1)
            while num[l]:
                x=heapq.heappop(num[l])
                ans.append(x)
                y=heapq.heappop(num[l])
                ans.append(y)
                for j in range(l-1,0,-1):
                    if num[j] and j!=1:
                        a=heapq.heappop(num[j])
                        b=heapq.heappop(num[j])
                        ans.append(b)
                        ans.append(a)
                        break
                    elif num[j]:
                        num[1].clear()
                        ans.append(1)
                        break
                
    if behind:
        ans.append(behind)
        
    print(*ans)