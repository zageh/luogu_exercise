# P/*1141 01迷宫

## 题目描述

有一个仅由数字 $0$ 与 $1$ 组成的 $n \times n$ 格迷宫。若你位于一格 $0$ 上，那么你可以移动到相邻 $4$ 格中的某一格 $1$ 上，同样若你位于一格 $1$ 上，那么你可以移动到相邻 $4$ 格中的某一格 $0$ 上。

你的任务是：对于给定的迷宫，询问从某一格开始能移动到多少个格子（包含自身）。

## 输入格式

第一行为两个正整数 $n,m$。

下面 $n$ 行，每行 $n$ 个字符，字符只可能是 $0$ 或者 $1$，字符之间没有空格。

接下来 $m$ 行，每行两个用空格分隔的正整数 $i,j$，对应了迷宫中第 $i$ 行第 $j$ 列的一个格子，询问从这一格开始能移动到多少格。

## 输出格式

$m$ 行，对于每个询问输出相应答案。

## 输入输出样例 #1

### 输入 #1

```
2 2
01
10
1 1
2 2

```

### 输出 #1

```
4
4

```

## 说明/提示

对于样例，所有格子互相可达。

- 对于 $20\%$ 的数据，$n \leq 10$；
- 对于 $40\%$ 的数据，$n \leq 50$；
- 对于 $50\%$ 的数据，$m \leq 5$；
- 对于 $60\%$ 的数据，$n,m \leq 100$；
- 对于 $100\%$ 的数据，$1\le n \leq 1000$，$1\le m \leq 100000$。*/
#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,m;
    cin>>n>>m;
    
     vector<string> g(n);
    for(int i=0;i<n;i++){
        cin>>g[i];
    }

    vector<int> sz;
    vector<vector<int>> id(n+1,vector<int>(n+1,-1));
    
    int dx[4]={1,-1,0,0};
    int dy[4]={0,0,1,-1};

    int comp=0;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(id[i][j]!=-1){
                continue;
            }
            queue<pair<int,int>> q;
            q.push({i,j});
            int cnt=1;
            id[i][j]=comp;
            
            while(!q.empty()){
                auto cur=q.front();
                q.pop();
                int cx=cur.first,cy=cur.second;

                for(int a=0;a<4;a++){
                    int nx=cx+dx[a];
                    int ny=cy+dy[a];

                    if(nx<0||nx>=n||ny<0||ny>=n){
                        continue;
                    }
                    if(id[nx][ny]!=-1){
                        continue;
                    }
                    if(g[cx][cy]!=g[nx][ny]){
                        cnt++;
                        id[nx][ny]=comp;
                        q.push({nx,ny});
                    }
                }
            }
            comp++;
            sz.push_back(cnt);
        }
    }

    while(m--){
        int x,y;
        cin>>x>>y;
        cout<<sz[id[x-1][y-1]]<<'\n';
    }

    return 0;
    
}