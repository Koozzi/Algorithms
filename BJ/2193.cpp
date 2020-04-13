#include <iostream>

using namespace std;

int M;
long long int dp[91][2];

int main(){
    cin >> M;
    dp[1][1] = 1;
    dp[2][0] = 1;
    dp[3][0] = 1;
    dp[3][1] = 1;
    for(int i = 4 ; i <= M ; i++){
        dp[i][0] = dp[i-1][1] + dp[i-1][0];
        dp[i][1] = dp[i-1][0];
    }
    cout << dp[M][0] + dp[M][1] << "\n";
    return 0;
}