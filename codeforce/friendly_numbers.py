import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    x=input()
    n=int(x)
    count=0
    for i in range(n+1,n+100):
        digit_sum=0
        for num in str(i):
            digit_sum+=int(num)
        if digit_sum==i-n:
            count+=1
    print(count)