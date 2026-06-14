#include<bits/stdc++.h>
using namespace std;

int main(){
    int q;
    cin >> q;

    list<int> l;
    list<int>::iterator it = l.end();

    while (q --){
        int op;
        cin >> op;

        if (!op){
            int x;
            cin >> x;

            it = l.insert(it, x);
        }

        else if (op == 1){
            int d;
            cin >> d;
            advance(it, d);
        }

        else{
            if (it != l.end()) it = l.erase(it); 
        }    
    }

    for (int x : l){
        cout << x << '\n';
    }
    cout << '\n';

    return 0;
}