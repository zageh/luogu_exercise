#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, ans = -1e9;
    cin >> n;

    int g[n + 1][n + 1], pre[n + 1][n + 1];
    for (int i = 0; i <= n; i ++){
        g[i][0] = 0;
        g[0][i] = 0;
        pre[i][0] = 0;
        pre[0][i] = 0;
    }
    
    for (int i = 1; i <= n; i ++){
        for (int j = 1; j <= n; j ++){
            cin >> g[i][j];

            pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + g[i][j];
        }
    }
    
    for (int i = 1; i <= n; i ++){
        for (int j = 1; j <= n; j ++){
            for (int x = i; x <= n; x ++){
                for (int y = j; y <= n; y ++){
                    ans = max(ans, pre[x][y] - pre[i - 1][y] - pre[x][j - 1] + pre[i - 1][j - 1]);
                }
            }
        }
    }
    cout << ans;

    return 0;
}

