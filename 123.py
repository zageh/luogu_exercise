import sys
input = sys.stdin.readline
import math
  
ans = []  

n = int(input())
query = []

for _ in range(n):
    l, r = map(int, input().split())
    
    l -= 1
    
    ml, mr = (math.isqrt(8 * l + 1) - 1) // 2, (math.isqrt(8 * r + 1) - 1) // 2
    
    reml = l - ml * (ml + 1) // 2
    remr = r - mr * (mr + 1) // 2
     
    sumr = mr * (mr + 1) * (mr + 2) // 6 + remr * (remr + 1) // 2
    suml = ml * (ml + 1) * (ml + 2) // 6 + reml * (reml + 1) // 2
    
    ans.append(str(sumr - suml))

sys.stdout.write('\n'.join(ans))