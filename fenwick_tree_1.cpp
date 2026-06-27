#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int lowbit(int x){
    return x & (-x);
}

int n;
vector<ll> tr;

void add (int x, ll d){
    while (x <= n){
        tr[x] += d;
        x += lowbit(x);
    }
}

ll sum (int x){
    ll res = 0;
    while (x > 0){
        res += tr[x];
        x -= lowbit(x);
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;

    cin >> n >> m;
    tr.assign(n + 1, 0);

    for (int i = 1; i <= n; ++ i){
        int x;
        cin >> x;
        add(i, x);
    }

    for (int i = 0; i < m; ++ i){
        int op, u, v;
        cin >> op >> u >> v;

        if (op == 1){
            add(u, v);
        }else{
            cout << sum(v) - sum(u - 1) << '\n';
        }
    }

    return 0;
}