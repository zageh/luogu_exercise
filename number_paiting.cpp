#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int mod = 998244353;

int main(){
    int n;
    ll s = 0;
    scanf("%d", &n);

    vector<int> a(n);
    for (int i = 0; i < n; ++ i){
        scanf("%d", &a[i]);
        s = s + a[i];
    }

    int l = 0, r = 0;
    ll mid = s >> 1;
    ll cur = a[0], curl = s - cur;
    ll mx = cur;
    ll mn = s;

    if (cur > mid){
        printf("%lld", (cur % mod) * (curl % mod) % mod);
        return 0;
    }

    while (r < n){
        if (cur == mid){
            mx = cur;
            break;
        }

        while (r < n && cur < mid){
            mx = max(cur, mx);
            r ++;
            if (r < n){
                cur = cur + a[r];
            }
        }
        while (l <= r && cur > mid){
            mn = min(mn, cur);
            cur -= a[l];
            l ++;
        }
    }

    if (2 * mn - s < s - 2 * mx){
        mx = mn;
    }

    curl = s - mx;
    ll ans = curl % mod * (mx  % mod)% mod;
    printf("%lld", ans);

    return 0;
}