#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d", &n);

    vector<pair<int, int>> p;
    for (int i = 0; i < n; ++ i){
        int h, l;
        scanf("%d%d", &h, &l);
        p.push_back({l, h});
    }

    sort(p.begin(), p.end());

    int mx = 0;
    for (int i = n - 1; i > -1; --i){
        if (mx > p[i].second){
            p[i].second = 0; 
        }
        else{
            mx = p[i].second;
        }
    }

    int q;
    scanf("%d", &q);
    vector<int> ans(q);
    vector<pair<int,int>> t;

    for (int i = 0; i < q; ++ i){
        int x;
        scanf("%d", &x);
        t.push_back({x, i});
    }

    sort(t.begin(), t.end());

    int idx = 0;
    for (int i = 0; i < n; ++ i){
        int curt = p[i].first;
        int curh = p[i].second;
        if (!curh) continue;

        while (idx < q && t[idx].first < curt){
            int j = t[idx].second;
            ans[j] = curh;
            idx ++;
        }
    }

    for (int x : ans){
        printf("%d\n", x);
    }

    return 0;
}