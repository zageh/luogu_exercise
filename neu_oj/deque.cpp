#include<bits/stdc++.h>
using namespace std;

int main(){
    int q;
    cin >> q;
    deque<int> dq;

    while(q --){
        int op;
        cin >> op;

        if (!op){
            int d, x;
            cin >> d >> x;
            if (!d) dq.push_front(x);
            else dq.push_back(x);
        }

        else if (op == 1){
            int p;
            cin >> p;
            cout << dq[p] <<'\n';
        }

        else {
            int d;
            cin >> d;

            if (!d) dq.pop_front();
            else dq.pop_back();
        }
    }

    return 0;
}