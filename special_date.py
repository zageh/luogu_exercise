import datetime as dt

def add(s:str)->int:
    n=0
    for x in s:
        n+=int(x)
    return n

start=dt.date(2000,1,1)
end=dt.date(9999,1,1)

cur=start
cnt=0
while cur<=end:
    y=str(cur.year)
    m=str(cur.month)
    d=str(cur.day)
    
    if add(y)==add(m)+add(d):
        cnt+=1
        
    cur+=dt.timedelta(days=1)
        
print(cnt)