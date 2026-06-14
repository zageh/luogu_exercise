#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, c, ans = 0;
    vector<int> dp(20000, -1);
    dp[0] = 0;

    cin >> n >> c;

    for (int i = 0; i < n; ++ i){
        int v, w;
        cin >> v >> w;

        for (int j = c; j >= w; -- j){
            if (dp[j - w] >= 0){
                dp[j] = max(dp[j - w] + v, dp[j]);
                ans = max(ans, dp[j]);
            } 
        }
    }

    cout << ans;

    return 0;
}