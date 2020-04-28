#include <iostream>
#include <algorithm>
#define MOD 1000000007
using namespace std;

int T, M;
long long dp[5001];

void DP(){
    dp[0] = 1;
    for(int i = 2 ; i <= 5000 ; i+= 2){
        for(int k = 2 ; k <= i ; k += 2){
            dp[i] = (dp[i] + dp[k-2]*dp[i-k]) % MOD;
        }
        dp[i] %= MOD;
    }
}

int main(){
    DP();
    cin >> T;
    while(T--){
        cin >> M;
        cout << dp[M] << "\n";
    }
    return 0;
}