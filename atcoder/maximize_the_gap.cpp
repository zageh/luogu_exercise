#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int>> p;
int n, k;

bool check(int y){
    int x = k - 1;
    int end = p[0].second;
    for (int i = 1; i < n; ++ i){
        if (p[i].first >= end + y){
            x --;
            end = p[i].second;
            if (x == 0) break;
        }
    }

    return x == 0 ? true : false;
}

int main(){
    scanf("%d%d", &n, &k);

    int l = 0, r = 0;

    for (int i = 0; i < n; ++ i){
        int a, b;
        scanf("%d%d", &a, &b);

        r = max(r, b);

        p.push_back({a, b});
    }

    sort(p.begin(), p.end(), [](const pair<int, int>& a,const pair<int, int>& b){
        return a.second < b.second;
    });

    while (l < r){
        int mid = (l + r + 1) >> 1;
        if (check(mid)){
            l = mid;
        }
        else{
            r = mid - 1;
        }
    }
    
    int ans = check(1) ? l : -1; 

    printf("%d\n", ans);

    return 0;
}