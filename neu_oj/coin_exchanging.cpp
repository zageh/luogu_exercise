#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, m, d[21];
    cin >> n >> m;

    vector<int> dp(60005, 100000000);
    dp[0] = 0;

    for (int i = 0; i < m; ++ i){
        cin >> d[i];
    }

    for (int i = 0; i <= n; ++ i){
        for (int j = 0; j < m; ++ j){
            dp[i + d[j]] = min(dp[i + d[j]], dp[i] + 1);
        }
    }
    cout << dp[n];

    return 0;
}