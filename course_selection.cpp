#include<bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int> > dp;
vector<vector<int> > son;
vector<int> score;

const int inf = -300 * 300 - 5;

void dfs(int p){
    if (p == 0) dp[p][0] = 0;
    else dp[p][1] = score[p];

    for (int & s: son[p]){
        dfs(s);

        for (int i = m; i >= 0; -- i){
            for (int j = 1; j <= m - i; ++ j){
                dp[p][i + j] = max(dp[p][i + j], dp[p][i] + dp[s][j]);
            }
        }
    }
}

int main(){
    scanf("%d%d", &n, &m);

    dp.assign(n+1, vector<int> (m+2, inf));
    son.assign(n+1, vector<int> ());
    score.assign(n+1, 0);

    int x, y;
    for (int i = 0; i < n; ++ i){
        scanf("%d%d", &x, &y);
        son[x].push_back(i + 1);
        score[i + 1] = y;
    }

    dfs(0);

    printf("%d", dp[0][m]);

    return 0;
}