#include<bits/stdc++.h>
using namespace std;
#define MAXN 200005

int main(){
    int n, h[MAXN], dp[MAXN], h1, h2;
    cin >> n;
    
    cin >> h1 >> h2;
    h[1] = h1;
    h[2] = h2;
    dp[1] = 0;
    dp[2] = abs(h1 - h2);

    for (int i = 3; i < n + 1; ++i){
        int cur_h;
        cin >> cur_h;

        dp[i] = min(dp[i-1] + abs(h[i-1] - cur_h),
                    dp[i-2] + abs(h[i-2] - cur_h));
        h[i] = cur_h;
    }

    cout << dp[n];
    
    return 0;
}