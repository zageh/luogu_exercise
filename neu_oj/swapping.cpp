#include<bits/stdc++.h>
using namespace std;

int main(){
    string x;

    cin >> x;
    int n = x.size();

    string t = x + x;

    int i = 0, j = 1, k = 0;
    while (i < n && j < n && k < n){
        if (t[i + k] == t[j + k]){
            k ++;
        }

        else if (t[i + k] > t[j + k]){
            i = i + k + 1;
            if (i == j) i ++;
            k = 0;
        }

        else{
            j = j + k + 1;
            if (i == j) j ++;
            k = 0;
        }
    }

    int pos = min(i, j);

    for (int i = 0; i < n ;i ++){
        cout << t[pos + i];
    }

    return 0;
}