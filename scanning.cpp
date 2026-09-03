#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, k;
    scanf("%d%d", &n, &k);

    priority_queue<int> pq;
    priority_queue<int> wait;
    vector<int> b(n);

    for (int i = 0; i < n; ++ i){
        scanf("%d", &b[i]);
        if (i < k) pq.push(b[i]);
    }

    int l = 0, r = k - 1;

    printf("%d\n", pq.top());

    int t = n - k;
    while (t --){
        wait.push(b[l]);

        l ++;
        r ++;

        pq.push(b[r]);
        
        while (!wait.empty() && 
                !pq.empty() && wait.top() == pq.top()){
            pq.pop();
            wait.pop();
        }

        printf("%d\n", pq.top());
    }
  
    return 0;
}