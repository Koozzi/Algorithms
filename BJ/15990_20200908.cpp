#include <iostream>
#define DIV_NUM 1000000009
using namespace std;

long long dp[100001][4];

int main(){
    int T; cin >> T;

    dp[1][1] = 1;
    dp[2][2] = 1;
    dp[3][1] = 1;
    dp[3][2] = 1;
    dp[3][3] = 1;

    for(int i = 4 ; i <= 100000 ; i++){
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % DIV_NUM;
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % DIV_NUM;
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % DIV_NUM;
    }

    while(T--){
        int N; cin >> N;
        cout << (dp[N][1] + dp[N][2] + dp[N][3]) % DIV_NUM << "\n";
    }
}