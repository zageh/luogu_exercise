#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v;

    int q;
    cin >> q;

    for (int i = 0; i < q; ++ i){
        int op;
        cin >> op;

        if (!op){
            int x;
            cin >> x;
            v.push_back(x);
        }

        else if (op == 1){
            int p;
            cin >> p;
            cout << v[p] << endl;
        }

        else{
            if (!v.empty()) v.pop_back();
        }
    }

    return 0;
}