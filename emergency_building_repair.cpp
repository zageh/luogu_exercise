#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
    int n;
    ll cur = 0;
    scanf("%d", &n);

    vector<pair<int, int> > t(n);
    priority_queue<int> cost;
    for (int i = 0; i < n; ++ i){
        scanf("%d%d", &t[i].second, &t[i].first);
    }

    sort(t.begin(), t.end());

    for (auto &a : t){
        cur += a.second;
        cost.push(a.second);
        if (cur > a.first){
            cur -= cost.top();
            cost.pop();
        }
    }

    printf("%d", cost.size());

    return 0;
}