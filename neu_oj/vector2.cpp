#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, q;
    cin >> n >> q;

    vector<vector<int>> v(n, vector<int> ());

    for (int i = 0; i < q; ++ i){
        int op;
        cin >> op;

        if (!op){
            int t, x;
            cin >> t >> x;
            v[t].push_back(x);
        }

        else if (op == 1){
            int l, t;
            cin >> t;

            l = v[t].size();

            for (int j = 0; j < l; ++ j) cout << v[t][j] << ' ';

            cout << '\n';
        }

        else{
            int t;
            cin >> t;
            if (!v[t].empty()) v[t].clear();
        }
    }

    return 0;
}