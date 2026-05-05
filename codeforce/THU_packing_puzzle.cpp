#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;

    while(t--){
        int t,h,u;
        cin>>t>>h>>u;
        int ans = 0;

        if(t > u + 2 * h){
            cout<<2 * t + 2 * u + 3 * h + 1<<'\n';
        }

        else{
            cout<<2 * t + 3 * u + 3 * h -min(t,u)<<'\n'; 
        }
    }

    return 0;
}