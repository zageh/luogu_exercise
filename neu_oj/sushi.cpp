#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, c1 = 0, c2 = 0, c3 = 0;
    cin >> n;

    int a[n + 5];
    for (int i = 0; i < n; i ++){
        cin >> a[i];
        if (a[i] == 1) c1 ++;
        if (a[i] == 2) c2 ++;
        if (a[i] == 3) c3 ++;
    }

    vector<vector<vector<double>>> dp(n + 2,vector<vector<double>>(n + 2, vector<double>(c3 + 2, 0.0)));

    for (int k = 0; k <= c3; k ++){
        for (int j = 0; j <= n; j ++){
            for (int i = 0; i <= n; i++){
                if (i + j + k == 0) continue;
                if (i + j + k > n) continue;

                double d = n;

                if (i > 0) d += dp[i - 1][j][k] * i;
                if (j > 0) d += dp[i + 1][j - 1][k] * j;
                if (k > 0) d += dp[i][j + 1][k - 1] * k;

                dp[i][j][k] = d / (i + j + k);
            }
        }
    }

    cout << dp[c1][c2][c3] << endl;

    return 0;
}