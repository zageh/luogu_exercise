#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, c;
    scanf("%d%d", &n, &c);

    vector<int> dp(c + 1, 0);

    for (int i = 0; i < n; ++ i){
        int v, w, m;
        scanf("%d%d%d", &v, &w, &m);


        int d = 1;
        while (0 < m){
            int p = min(d, m);
            d <<= 1;
            m -= p;

            for (int j = c; j >= p * w; -- j){
                dp[j] = max(dp[j], dp[j - p * w] + v * p);
            }
        }
    }

    int ans = 0;
    for (int i = 1; i < c + 1; ++ i){
        if (dp[i] > ans) ans = dp[i];
    }

    printf("%d\n", ans);

    return 0;
}