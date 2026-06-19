#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; ++ i) cin >> a[i];

    vector<bool> dp(k + 1, false);

    for (int i = 1; i <= k; ++ i){
        for (int x : a){
            if (i < x) break;

            if (!dp[i - x]){
                dp[i] = true;
                break;
            }
        }
    }

    cout << (dp[k] ? "First" : "Second") << endl;

    return 0;
}