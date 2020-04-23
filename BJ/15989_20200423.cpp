#include <iostream>
#define MAX_NUM 10001
using namespace std;

int T, M;
long long int dp[4][MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    dp[1][1] = 1;
    dp[1][2] = 1;
    dp[2][2] = 1;
    dp[1][3] = 1;
    dp[2][3] = 1;
    dp[3][3] = 1;
    for(int i = 4 ; i < MAX_NUM ; i++){
        dp[1][i] = 1;
        dp[2][i] = dp[1][i-2] + dp[2][i-2];
        dp[3][i] = dp[1][i-3] + dp[2][i-3] + dp[3][i-3];
    }
    cin >> T;
    while(T--){
        cin >> M;
        cout << dp[1][M] + dp[2][M] +dp[3][M] << "\n";
    }
    return 0;
}