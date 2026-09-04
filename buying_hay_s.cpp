#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, H;
    cin >> n >> H;

    vector<pair<int,int>> hay(n);

    int mx = 0;

    for(auto &[p,c]: hay){
        cin >> p >> c;
        mx = max(mx,p);
    }

    const int INF = 50000 * 5000 + 5;

    vector<int> dp(H + mx + 1, INF);

    dp[0] = 0;

    for(auto &[p,c]: hay){
        for(int j = p; j <= H + mx; j++){
            dp[j] = min(dp[j], dp[j-p] + c);
        }
    }

    int ans = INF;

    for(int i = H; i <= H + mx; i++){
        ans = min(ans, dp[i]);
    }

    cout << ans << endl;

    return 0;
}