#include<bits/stdc++.h>
using namespace std;

int main(){
    int m, s, c, mx = 0, mn = 205;
    scanf("%d%d%d", &m, &s, &c);

    vector<int> p(c);

    for (int i = 0; i < c; ++ i){
        scanf("%d", &p[i]);

        mx = max(mx, p[i]);
        mn = min(mn, p[i]);
    }

    sort(p.begin(), p.end());

    if (m >= c){
        printf("%d", c);
        return 0;
    }

    vector<int> mid;

    for (int i = 1; i < c; ++ i){
        int x = p[i] - p[i - 1] - 1;
        mid.push_back(x);
    }

    sort(mid.rbegin(),mid.rend());

    int saved = 0;

    for (int i = 0; i < m - 1; ++ i){
        saved += mid[i];
    }

    printf("%d", mx - mn - saved + 1);

    return 0;
}