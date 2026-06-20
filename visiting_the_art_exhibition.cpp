#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, m;
    scanf("%d%d", &n, &m);

    vector<int> a(n + 1);
    for (int i = 0; i < n; ++ i){
        scanf("%d", &a[i]);
    }

    int l = 0, r = 0, cnt = 1, mn = 10000000;
    int lans = 0, rans = 0;
    vector<int> vis(n + 1, 0);
    vis[a[0]] = 1;
    
    while (true){
        if (r >= n) break;
        if (cnt < m){
            r ++;
            if (!vis[a[r]]){
                cnt ++;
            }
            vis[a[r]] ++;
        }
        else{
            if (r - l + 1< mn){
                mn = r - l + 1;
                lans = l + 1;
                rans = r + 1;
            }

            vis[a[l]] --;
            if (!vis[a[l]]){
                cnt --;
            }

            l ++;
        }
    }

    printf("%d %d\n", lans, rans);

    return 0;
}