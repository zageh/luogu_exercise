#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<double> p(n + 1);
    for (int i = 1; i <= n; ++ i){
        cin >> p[i];
    }

    vector<vector<double>> dp(n + 1, vector<double> (n + 1, 0.0));
    dp[0][0] = 1.0;

    for (int i = 1; i <= n ; ++ i){
        for (int j = 0; j <= i; ++ j){
            dp[i][j] = dp[i - 1][j] * (1 - p[i]);

            if (j) dp[i][j] += dp[i - 1][j - 1] * p[i];
        }
    }

    int lim = (n >> 1);

    double ans = 0.0;
    for (int i = lim + 1; i <= n; ++ i){
        ans += dp[n][i] * 1.0;
    }

    cout << setprecision(15) << ans << endl;

    return 0;
}