#include<bits/stdc++.h>
using namespace std;

vector<int> primes;
vector<bool> is_prime(1005, true);

int main(){
    int n;
    cin >> n;

    vector<long long> dp(n + 1);

    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i < 1001; ++ i){
        if (is_prime[i]){
            primes.push_back(i);
            
            for(int j = i * i; j < 1001; j += i){
                is_prime[j] = false;
            }
        }
    }

    dp[0] = 1;
    for (int &p : primes){
        for (int j = p; j <= n; ++ j){
            dp[j] += dp[j - p];
        }
    }

    cout << dp[n] << endl;

    return 0;
}