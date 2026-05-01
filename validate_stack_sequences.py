from collections import deque
import sys
input=sys.stdin.readline

q=int(input().strip())
for _ in range(q):
    n=int(input().strip())
    l1=list(map(int,input().strip().split()))
    l2=list(map(int,input().strip().split()))
    qin=deque(l1)
    qout=deque(l2)

    wait=[]
    while qin:
        x=qin.popleft()
        y=qout.popleft()
        if x==y:
            while wait:
                a=wait.pop()
                b=qout.popleft()
                if a!=b:
                    qout.appendleft(b)
                    wait.append(a)
                    break
        else:
            wait.append(x)
            qout.appendleft(y)
    
    print("No" if wait else "Yes")