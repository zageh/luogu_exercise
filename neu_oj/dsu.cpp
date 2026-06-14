#include<bits/stdc++.h>
using namespace std;

int p[10005];
int find(int x){
    while (p[x] != x){
        p[x] = p[p[x]];
        x = p[x];
    }

    return p[x];
}

void unite(int x, int y){
    int fx = find(x), fy = find(y);
    p[fy] = fx;
}

bool same(int x, int y){
    return find(x) == find(y);
}

int main(){
    int n, q;
    cin >> n >> q;

    for (int i = 0; i <=n; ++ i){
        p[i] = i;
    }

    while(q --){
        int op, x, y;
        cin >> op >> x >> y;
        
        if (op){
            if (same(x, y)) cout << 1 << '\n';        
            else cout << 0 << '\n';
        }

        else unite(x, y);
    }

    return 0;
}