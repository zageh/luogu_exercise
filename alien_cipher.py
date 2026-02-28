import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

s=input().strip()
n=len(s)
def parse(i:int):
    parts=[]
    while i<n and s[i]!=']':
        if 'A'<=s[i]<='Z':
            parts.append(s[i])
            i+=1
        elif s[i]=='[':
            i+=1
            d=0
            while i<n and s[i].isdigit():
                d=d*10+ord(s[i])-48
                i+=1

            inner,i=parse(i)
            i+=1

            parts.append(inner*d)
    return(''.join(parts),i)

ans,_=parse(0)
print(ans)