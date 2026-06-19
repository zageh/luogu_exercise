#include<bits/stdc++.h>
using namespace std;

using ll = long long;

const int mod = 1000000007;

int main(){
    int h, w;

    cin >> h >> w;

    vector<string> b(h);
    vector<vector<ll> > dp(h, vector<ll> (w, 0));
    dp[0][0] = 1;

    for (int i = 0; i < h; ++ i){
        cin >> b[i];
    }
    if (b[0][0] == '#'){
        cout << 0 << endl;
        return 0;
    }

    for (int i = 0; i < h; ++ i){
        for (int j = 0; j < w; ++ j){
            if (b[i][j] == '.'){
                if (i) dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod;
                if (j) dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod;
            }
        }
    }

    cout << dp[h-1][w-1] << endl;

    return 0;

}