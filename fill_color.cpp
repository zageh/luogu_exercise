/*# P1162 填涂颜色

## 题目描述

由数字 $0$ 组成的方阵中，有一任意形状的由数字 $1$ 构成的闭合圈。现要求把闭合圈内的所有空间都填写成 $2$。例如：$6\times 6$ 的方阵（$n=6$），涂色前和涂色后的方阵如下：

如果从某个 $0$ 出发，只向上下左右 $4$ 个方向移动且仅经过其他 $0$ 的情况下，无法到达方阵的边界，就认为这个 $0$ **在闭合圈内**。闭合圈不一定是环形的，可以是任意形状，但保证**闭合圈内**的 $0$ 是连通的（两两之间可以相互到达）。

```plain
0 0 0 0 0 0
0 0 0 1 1 1
0 1 1 0 0 1
1 1 0 0 0 1
1 0 0 1 0 1
1 1 1 1 1 1
```
```plain
0 0 0 0 0 0
0 0 0 1 1 1
0 1 1 2 2 1
1 1 2 2 2 1
1 2 2 1 2 1
1 1 1 1 1 1
```

## 输入格式

每组测试数据第一行一个整数 $n(1 \le n \le 30)$。

接下来 $n$ 行，由 $0$ 和 $1$ 组成的 $n \times n$ 的方阵。

方阵内只有一个闭合圈，圈内至少有一个 $0$。

## 输出格式

已经填好数字 $2$ 的完整方阵。

## 输入输出样例 #1

### 输入 #1

```
6
0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 0 0 1
1 1 0 0 0 1
1 0 0 0 0 1
1 1 1 1 1 1

```

### 输出 #1

```
0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 2 2 1
1 1 2 2 2 1
1 2 2 2 2 1
1 1 1 1 1 1

```

## 说明/提示

对于 $100\%$ 的数据，$1 \le n \le 30$。*/
#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int dx[4]={1,0,0,-1};
    int dy[4]={0,-1,1,0};
    
    int n;
    cin>>n;
    vector<vector<int>> v(n,vector<int> (n,0));
    vector<vector<bool>> b(n,vector<bool> (n,false));
    queue<pair<int,int>> q;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>v[i][j];
            if((i==0||j==0||i==n-1||j==n-1)&&v[i][j]==0){
                b[i][j]=true;
                q.push({i,j});
            }
        }
    }

    while(!q.empty()){
        auto cur=q.front();
        q.pop();

        int cx=cur.first;
        int cy=cur.second;

        for(int i=0;i<4;i++){
            int nx=cx+dx[i];
            int ny=cy+dy[i];

            if(nx>=0&&nx<n&&ny>=0&&ny<n){
                if(v[nx][ny]==0&&b[nx][ny]==false){
                    b[nx][ny]=true;
                    q.push({nx,ny});
                }
            }
        }
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(v[i][j]==0&&b[i][j]==false){
                cout<<2<<' ';
            }
            else{
                cout<<v[i][j]<<' ';
            }
        }
        cout<<'\n';
    }

    return 0;
}