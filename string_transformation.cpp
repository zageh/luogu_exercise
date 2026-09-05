#include<bits/stdc++.h>
using namespace std;

vector<pair<string,string>> rule1, rule2;

int bfs(queue<string>& q,
        unordered_map<string,int>& da,
        unordered_map<string,int>& db,
        vector<pair<string,string>>& rules)
{
    int x = q.size();

    while(x--){
        string cur = q.front();
        q.pop();

        int step = da[cur];

        if(step>=10) continue;

        for (auto &[from, to] : rules){

            int len=from.size();

            for (int i=0; i+len<=cur.size(); ++ i){
                if(cur.substr(i, len) == from){
                    string nxt = cur;

                    nxt.replace(i, len, to);

                    if(db.count(nxt)){
                        return step + 1 + db[nxt];
                    }

                    if(!da.count(nxt)){
                        da[nxt] = step + 1;
                        q.push(nxt);
                    }
                }
            }
        }
    }
    return -1;
}

int main(){

    string A, B;
    cin >> A >> B;

    string x, y;

    while(cin>>x>>y){
        rule1.push_back({x, y});
        rule2.push_back({y, x});
    }

    queue<string> q1,q2;

    unordered_map<string,int> d1,d2;

    q1.push(A);
    q2.push(B);

    d1[A]=0;
    d2[B]=0;

    while(!q1.empty() && !q2.empty()){
        int ans;

        if(q1.size() <= q2.size()){
            ans=bfs(q1, d1, d2, rule1);
        }
        else{
            ans=bfs(q2, d2, d1, rule2);
        }

        if(ans != -1){
            cout << ans << endl;
            return 0;
        }
    }

    cout<<"NO ANSWER!";

    return 0;
}