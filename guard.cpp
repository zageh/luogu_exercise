#include<iostream>
#include<vector>
#include<set>
#include<cmath>
#include<cstdio>
using namespace std;

struct guard{
public:
    int x,y;
    guard(int a=0,int b=0){
        x=a;
        y=b;
    }
    bool operator<(const guard& p) const {
        return x != p.x ? x < p.x : y < p.y;
    }
};

int main(){
    int n;
    cin>>n;
    long long sum1=0,sum2=0;
    int avgX2,avgY2;
    vector<guard> g;
    for(int i=0;i<n;i++){
        int a,b;
        cin>>a>>b;
        sum1+=a;
        sum2+=b;
        g.push_back(guard(a,b));
    }
    avgX2=2*sum1/n;
    avgY2=2*sum2/n;
    if (2*sum1 % n != 0 || 2*sum2% n != 0) {
        cout << "This is a dangerous situation!" << endl;
        return 0;
    }
    set<guard> gu(g.begin(),g.end());
    bool valid=true;
    for(int i=0;i<n;i++){
        guard aim=guard(avgX2-g[i].x,avgY2-g[i].y);
        if(gu.find(aim)==gu.end()){
            valid = false;
            break;
        }
    }
    if(valid){
        double avgX = (double)avgX2 / 2.0;
        double avgY = (double)avgY2 / 2.0;
        if (fabs(avgX) < 0.0001) avgX = 0.0;
        if (fabs(avgY) < 0.0001) avgY = 0.0;
        printf("V.I.P. should stay at (%.1f,%.1f).\n", avgX,avgY);
    }
    else{
        cout<<"This is a dangerous situation!"<<endl;
    }
    return 0;
}
