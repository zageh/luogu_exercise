import sys
sys.set_int_max_str_digits(0)
from functools import cmp_to_key
input=sys.stdin.readline

n=int(input().strip())
lst=[]
for i in range(1,n+1):
    lst.append(bin(i)[2:])

def cmp(a:str,b:str):
    if a+b>b+a:
        return -1
    elif a+b<b+a:
        return 1
    else:
        return 0

lst.sort(key=cmp_to_key(cmp))

ans=0
for nums in lst:
    num=int(nums,2)
    ans=(ans<<num.bit_length())|num
print(ans)