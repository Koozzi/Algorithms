#include <iostream>
using namespace std;

long long dp[1000001];

int main(){
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i = 4 ; i <= 1000000 ; i++){
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009;
    }
    int T; cin >> T;
    while(T--){
        int N; cin >> N;
        cout << dp[N] << "\n";
    }
    return 0;
}