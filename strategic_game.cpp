#include<bits/stdc++.h>
using namespace std;

int n;
vector<vector<int> > g;
vector<array<int, 2> > dp;

void dfs(int u, int fa){
    dp[u][0] = 0;
    dp[u][1] = 1;

    for (int v: g[u]){
        if (v == fa) continue;

        dfs(v, u);

        dp[u][1] += min(dp[v][0], dp[v][1]);
        dp[u][0] += dp[v][1];
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    g.assign(n,{});
    dp.assign(n,{0, 0});

    for (int i = 0; i < n; ++ i){
        int d, t;
        cin >> d >> t;
        for (int j = 0; j < t; ++ j){
            int x;
            cin >> x;

            g[d].push_back(x);
            g[x].push_back(d);
        }
    }

    dfs(0, -1);

    cout << min(dp[0][0], dp[0][1]) << endl;

    return 0;
}