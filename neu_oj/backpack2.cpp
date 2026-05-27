#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    int n, limit, total = 0;
    cin >> n >> limit;

    int w[n + 1], v[n + 1];

    for (int i = 0; i < n; i ++){
        cin >> w[i] >> v[i];
        total += v[i];
    }

    vector<ll> cost(total + 1, 1e18);
    cost[0] = 0;

    for (int i = 0; i < n; i ++){
        int val = v[i];
        int wei = w[i];
        for (int j = total; j >= val; j --){
            if (cost[j - val] == 1e18) continue;

            cost[j] = min(cost[j], cost[j - val] + wei);
        }
    }

    for (int i = total; i >= 0; i --){
        if (cost[i] <= limit){
            cout << i;
            break;
        } 
    }

    return 0;

}