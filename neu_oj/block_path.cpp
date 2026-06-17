#include<bits/stdc++.h>
using namespace std;

using ll = long long;

const int mod = 1000000007;

int qpow(ll a, ll b){
    ll res = 1;

    while (b){
        if (b & 1) res = res * a % mod;

        a = a * a % mod;
        b >>= 1;
    }

    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> p;

    for (int i = 0; i < m; ++ i){
        int y, x;
        cin >> y >> x;

        p.push_back({y, x});
    }

    p.push_back({n, n});

    sort(p.begin(), p.end());

    vector<ll> dp(p.size());
    
    int maxn = 2 * n +5;

    vector<ll> fac(maxn), ifac(maxn);

    fac[0] = 1;
    for (int i = 1; i < maxn; ++ i){
        fac[i] = fac[i - 1] * i % mod;
    }

    ifac[0] = 1;
    ifac[maxn - 1] = qpow(fac[maxn - 1], mod - 2);
    for (int i = maxn - 2; i >= 1; -- i){
        ifac[i] = ifac[i + 1] * (i + 1) % mod;
    }

    auto C = [&](int a, int b) -> ll{
        if (b < 0 || b > a) return 0;

        return fac[a] * ifac[b] % mod * ifac[a - b] % mod; 
    };

    auto ways = [&](pair<int, int> p1, pair<int, int> p2) -> ll{
        int x1 = p1.second, y1 = p1.first;
        int x2 = p2.second, y2 = p2.first;

        if (x1 > x2 || y1 > y2) return 0;

        int dx = x2 - x1;
        int dy = y2 - y1;

        return C(dx + dy, dx);
    };

    for (int i = 0; i < (int)p.size(); ++ i){
        dp[i] = ways({1, 1}, p[i]);

        for (int j = 0; j < i; ++ j){
            ll bad = dp[j] * ways(p[j], p[i]) % mod;
            dp[i] = (dp[i] - bad + mod) % mod; 
        }
    }

    cout << dp.back() << endl;

    return 0;
}