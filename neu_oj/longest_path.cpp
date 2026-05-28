#include<bits/stdc++.h>
using namespace std;

vector<int> dp;
vector<vector<int>> p;

int dfs(int i){
    if (dp[i] != -1){
        return dp[i];
    }

    int cand = 0;
    for (int v : p[i]){
        cand = max(cand, dfs(v) + 1);
    }

    return dp[i] = cand;
    }

int main(){
    int n, m;
    cin >> n >> m;

    p.resize(n + 1);
    dp.assign(n + 1, -1);

    for (int i = 0; i < m; i ++){
        int x, y;
        cin >> x >> y;

        p[y].push_back(x);
    }

    for (int i = 1; i < n + 1; i ++){
        dfs(i);
    }

    int ans = 0;

    for (int i = 1; i < n + 1; i ++){
        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}