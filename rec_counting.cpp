#include<bits/stdc++.h>
using namespace std;

using ll = long long;

const ll mod = 998244353;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    string up, down;
    cin >> up >> down;

    auto ok = [&](int i, int st) -> bool {
        int a = (st >> 1) & 1;
        int b = st & 1;

        if (up[i] != '?' && up[i] - '0' != a) return false;
        if (down[i] != '?' && down[i] - '0' != b) return false;

        return true;
    };

    auto trans = [&](int pre, int cur) -> bool {
        if (pre == 0 && cur == 0) return false; 
        if (pre == 3 && cur == 3) return false; 
        return true;
    };

    vector<ll> dp(4, 0), ndp(4, 0);

    for (int st = 0; st < 4; ++st) {
        if (ok(0, st)) {
            dp[st] = 1;
        }
    }

    for (int i = 1; i < n; ++i) {
        fill(ndp.begin(), ndp.end(), 0);

        for (int pre = 0; pre < 4; ++pre) {
            if (!dp[pre]) continue;

            for (int cur = 0; cur < 4; ++cur) {
                if (!ok(i, cur)) continue;
                if (!trans(pre, cur)) continue;

                ndp[cur] = (ndp[cur] + dp[pre]) % mod;
            }
        }

        dp = ndp;
    }

    ll ans = 0;
    for (int st = 0; st < 4; ++st) {
        ans = (ans + dp[st]) % mod;
    }

    cout << ans;

    return 0;
}