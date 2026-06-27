#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t --){
        int n;
        string s;
        cin >> n >> s;
        vector<ll> x(n), y(n);

        for (int i = 0; i < n; ++ i){
            cin >> x[i];
        }
        for (int i = 1; i < n; ++ i){
            cin >> y[i];
        }

        vector<vector<ll> > dp(n, vector<ll> (2, 0));

        if (s[0] == 'S'){
            dp[0][1] = -x[0];
        }else{
            dp[0][0] = -x[0];
        }

        for (int i = 1; i < n; ++ i){
            if (s[i] == 'R'){
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + y[i]) - x[i];
            }else{
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) - x[i];
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + y[i]);
            }
        }

        cout << max(dp[n - 1][0], dp[n - 1][1]) << '\n';
    }

    return 0;
}