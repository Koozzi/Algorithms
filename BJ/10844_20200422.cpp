#include <iostream>
#define DIV_NUM 1000000000
using namespace std;

int M;
long long dp[101][10], ans;

int main(){
    cin >> M;
    for(int i = 1 ; i < 10 ; i++){
        dp[1][i] = 1;
    }
    for(int i = 2 ; i < M+1 ; i++){
        ans = 0;
        dp[i][0] = dp[i-1][1];
        dp[i][9] = dp[i-1][8];
        for(int k = 1 ; k < 9 ; k++){
            dp[i][k] = (dp[i-1][k-1] + dp[i-1][k+1]) % DIV_NUM;
        }
    }

    for(int i = 0 ; i < 10 ; i++){
        ans = (ans + dp[M][i]) % DIV_NUM;
    }

    cout << ans << "\n";
    return 0;
}