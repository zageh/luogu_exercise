#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,c;
    cin>>n>>c;
    vector<long long> q;
    for (int i=0;i<n;i++){
        long long x;
        cin>>x;
        q.push_back(x);
    }
    sort(q.begin(),q.end());
    int l=0,r=0;
    long long ans=0;
    while(l<n&&r<n){
        if(l==r){r++;continue;}
        if(q[r]-q[l]<c){
            r++;
        }
        else if(q[r]-q[l]>c){
            l++;
        }
        else{
            long long al=q[l],br=q[r];
            long long cntA=0,cntB=0;
            while(l<n&&al==q[l]){
                cntA++;
                l++;
            }
            while(r<n&&br==q[r]){
                cntB++;
                r++;
            }
            ans+=cntA*cntB;
        }
    }
    cout<<ans<<endl;
    return 0;
}