#include<bits/stdc++.h>
using namespace std;

int main(){
    int c, l;
    scanf("%d%d", &c, &l);

    vector<pair<int, int> > cow(c);
    vector<pair<int, int> > spf(l);

    for (int i = 0; i < c; ++ i){
        scanf("%d%d", &cow[i].first, &cow[i].second);
    }
    for (int i = 0; i < l; ++ i){
        scanf("%d%d", &spf[i].first, &spf[i].second);
    }

    sort(cow.begin(), cow.end(), [] (auto &a, auto &b) {
        return a.second < b.second;
    });
    sort(spf.begin(), spf.end());

    int cnt = 0;
    for (auto cur : cow){
        int low = cur.first;
        int high = cur.second;

        for (auto &scr : spf){
            if (scr.second == 0) continue;
            if (scr.first < low) continue;
            if (scr.first > high) break;

            scr.second--;
            cnt++;
            break;
        }
    }

    printf("%d\n", cnt);

    return 0;
}
