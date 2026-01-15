/*# P1002 [NOIP 2002 普及组] 过河卒

## 题目描述

棋盘上 $A$ 点有一个过河卒，需要走到目标 $B$ 点。卒行走的规则：可以向下、或者向右。同时在棋盘上 $C$ 点有一个对方的马，该马所在的点和所有跳跃一步可达的点称为对方马的控制点。因此称之为“马拦过河卒”。

棋盘用坐标表示，$A$ 点 $(0, 0)$、$B$ 点 $(n, m)$，同样马的位置坐标是需要给出的。

![](https://cdn.luogu.com.cn/upload/image_hosting/ipmwl52i.png)

现在要求你计算出卒从 $A$ 点能够到达 $B$ 点的路径的条数，假设马的位置是固定不动的，并不是卒走一步马走一步。

## 输入格式

一行四个正整数，分别表示 $B$ 点坐标和马的坐标。

## 输出格式

一个整数，表示所有的路径条数。

## 输入输出样例 #1

### 输入 #1

```
6 6 3 3

```

### 输出 #1

```
6

```

## 说明/提示

对于 $100 \%$ 的数据，$1 \le n, m \le 20$，$0 \le$ 马的坐标 $\le 20$。

**【题目来源】**

NOIP 2002 普及组第四题*/
#include<bits/stdc++.h>
using namespace std;

long long dp[25][25];
bool ban[25][25];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m,n,x,y;
    cin>>n>>m>>x>>y;

    int dx[8]={1,-1,2,-2,1,-1,2,-2};
    int dy[8]={2,2,1,1,-2,-2,-1,-1};

    ban[x][y]=true;
    for(int i=0;i<8;i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(nx<=n&&nx>=0&&ny>=0&&ny<=m){
            ban[nx][ny]=true;
        }
    }
    dp[0][0]=ban[0][0]?0:1;

    for(int i=0;i<=n;++i){
        for(int j=0;j<=m;++j){
            if(ban[i][j])continue;
            if(i==0&&j==0)continue;
            if(j>0)dp[i][j]+=dp[i][j-1];
            if(i>0)dp[i][j]+=dp[i-1][j];
        }
    }
        
    cout<<dp[n][m]<<endl;
    return 0;
}