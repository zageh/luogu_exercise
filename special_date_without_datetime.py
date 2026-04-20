def gcd(x,y):
    if y>x:
        x,y=y,x
    while y>0:
        x,y=y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

ans=0

days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

for m in range(1,13):
    for d in range(1,days[m]+1):
        ans+=(1999999//lcm(m,d))-(1999//lcm(m,d))
        
for y in range(2030,2000000,58):
    if (y%4==0 and y%100!=0) or (y%400==0):
        ans+=1
        
ans+=1

print(ans)