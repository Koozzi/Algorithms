#include <iostream>
using namespace std;

long long dp[1001];

int main(){
    int N; cin >> N;
    dp[1] = 1;
    dp[2] = 3;
    for(int i = 3 ; i <= N ; i++){
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-2]) % 10007;
    }
    cout << dp[N] << "\n";
    return 0;
}