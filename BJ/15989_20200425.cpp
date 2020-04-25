#include <iostream>
using namespace std;

long long int dp[4][10001];

void DP(){
    dp[1][1] = 1;
    dp[1][2] = 1;
    dp[2][2] = 1;
    dp[1][3] = 1;
    dp[2][3] = 1;
    dp[3][3] = 1;
    for(int i = 4 ; i <= 10000 ; i++){
        dp[1][i] = 1;
        dp[2][i] = dp[1][i-2] + dp[2][i-2];
        dp[3][i] = dp[1][i-3] + dp[2][i-3] + dp[3][i-3];
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    DP();
    int T; cin >> T;
    while(T--){
        int a; cin >> a;
        cout << dp[1][a] + dp[2][a] + dp[3][a] << "\n";
    }
    return 0;
}