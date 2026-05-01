import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input())
    s=input().strip()
    left=len(s)%2
    ok=True
    kt=0
    if left==1:
        if s[0]=='b':
            ok=False
        kt=1
    
    for i in range(kt,n-1,2):
        if s[i]!='?' and s[i+1]!='?' and s[i]==s[i+1]:
            ok=False
            break
        else:
            pass
        
    print('YES' if ok else 'NO')