#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, c;
    cin >> n >> m >> c;

    vector<vector<int>> v(n, vector<int>(m, 0));
    vector<vector<int>> pref(n, vector<int>(m, 0));

    for (int i = 0; i < n; ++ i){
        for (int j = 0; j < m; ++ j){
            cin >> v[i][j];
        }
    }
    for (int i = 0; i < n; ++ i){
        for (int j = 0; j < m; ++ j){
            int d = v[i][j];
            if (i > 0) d += pref[i-1][j];
            if (j > 0) d += pref[i][j-1];
            if (i * j > 0) d -= pref[i - 1][j - 1];

            pref[i][j] = d;
        }
    }

    int x = 0, y = 0, mx = -1e9;

    for (int i = 0; i < n - c + 1; ++ i){
        for (int j = 0; j < m - c + 1; ++ j){
            int cur = pref[i + c - 1][j + c - 1]
                - (i > 0 ? pref[i - 1][j + c - 1] : 0)
                - (j > 0 ? pref[i + c - 1][j - 1] : 0)
                + (i > 0 && j > 0 ? pref[i - 1][j - 1] : 0);

            if (cur > mx){
                mx = cur;
                x = i;
                y = j;
            }
        }
    }

    cout << x + 1 << ' ' << y + 1 << endl;

    return 0;
}