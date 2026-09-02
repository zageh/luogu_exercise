#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int n = 1, m = 1;
ll s;
vector<pair<int, int> > st;
vector<pair<int, int> > itv;

ll check(int w) {
    vector<ll> preCnt(n + 1, 0);
    vector<ll> preVal(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        preCnt[i] = preCnt[i - 1];
        preVal[i] = preVal[i - 1];

        if (st[i].first >= w) {
            preCnt[i]++;
            preVal[i] += st[i].second;
        }
    }

    ll y = 0;

    for (auto &a : itv) {
        int l = a.first;
        int r = a.second;

        ll cnt = preCnt[r] - preCnt[l - 1];
        ll val = preVal[r] - preVal[l - 1];

        y += cnt * val;
    }

    return y;
}

int main(){
    scanf("%d%d%lld", &n, &m, &s);

    st.resize(n + 1);
    itv.resize(m);
    int wei = 1;

    for (int i = 1; i < n + 1; ++ i) {
        scanf("%d%d", &st[i].first, &st[i].second);
        wei = max(wei,st[i].first);
    }
    for (int i = 0; i < m; ++ i) scanf("%d%d", &itv[i].first, &itv[i].second);

    int l = 0, r = wei + 1;
    ll mn = LLONG_MAX;
    while (l <= r){
        int mid = (l + r) >> 1;
        ll x = check(mid);

        mn = min(mn, llabs(x - s));

        if (x < s) r = mid - 1;
        else l = mid + 1;
    }

    printf("%lld\n", mn);

    return 0;
}