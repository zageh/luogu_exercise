# # P3799 小 Y 拼木棒

# ## 题目背景

# 上道题中，小 Y 斩了一地的木棒，现在她想要将木棒拼起来。

# ## 题目描述

# 有 $n$ 根木棒，现在从中选 $4$ 根，想要组成一个正三角形，问有几种选法？

# 答案对 $10^9+7$ 取模。

# ## 输入格式

# 第一行一个整数 $n$。

# 第二行往下 $n$ 行，每行 $1$ 个整数，第 $i$ 个整数 $a_i$ 代表第 $i$ 根木棒的长度。

# ## 输出格式

# 一行一个整数代表答案。

# ## 输入输出样例 #1

# ### 输入 #1

# ```
# 4 
# 1
# 1
# 2
# 2
# ```

# ### 输出 #1

# ```
# 1
# ```

# ## 说明/提示

# #### 数据规模与约定

# - 对于 $30\%$ 的数据，保证 $n \le 5 \times 10^3$。
# - 对于 $100\%$ 的数据，保证 $1 \leq n \le 10^5$，$1 \le a_i \le 5 \times 10^3$。

# 关于标题：因为一些不可抗力的原因，名称进行了更改。深表歉意。
import sys

def C2(x:int)->int:
    return x*(x-1)//2

mod=10**9+7
data=list(map(int,sys.stdin.buffer.read().split()))
n=data[0]
a=data[1:]

maxa=max(a)

c=[0]*(maxa+1)
total=0
for i in a:
    c[i]+=1

C2_local=C2
for l in range(1,maxa+1):
    if c[l]<2:
        continue
    ll=C2_local(c[l])

    pairs=0
    for x in range(1,l//2+1):
        y=l-x
        if x<y:
            if c[x]>0 and c[y]>0:
                pairs+=c[x]*c[y]
        if x==y and c[x]>=2:
                pairs+=C2_local(c[x])
        
    total=(total+ll*(pairs%mod))%mod

print(total)
        
    