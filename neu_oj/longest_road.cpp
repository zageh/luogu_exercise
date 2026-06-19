#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int> > pout(n + 1);
    vector<int> indeg(n + 1, 0);
    vector<int> topo;
    queue<int> q;

    while (m --){
        int x, y;
        cin >> x >> y;

        indeg[y] ++;
        pout[x].push_back(y);
    }
    
    vector<int> dp(n + 1, 0);

    for (int i = 1; i < n + 1; ++ i){
        if (!indeg[i]){
            q.push(i);
        }
    }

    while (!q.empty()){
        int u = q.front(); q.pop();
        topo.push_back(u);

        for (int v : pout[u]){
            if (-- indeg[v] == 0) q.push(v);
        }
    }

    int ans = 0;

    for (int i = n - 1; i >= 0; -- i){
        int u = topo[i];

        for(int v : pout[u]) dp[u] = max(dp[u], dp[v] + 1);
    }

    for (int i = 1; i < n + 1; ++ i){
        ans = max(ans, dp[i]);
    }

    cout << ans << endl;

    return 0;
}