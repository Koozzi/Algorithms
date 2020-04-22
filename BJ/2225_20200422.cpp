#include <iostream>
#define DIV_NUM 1000000000
using namespace std;

int M, N;
long long dp[201][201];

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M+1 ; i++){
        dp[i][1] = 1;
    }
    for(int i = 0 ; i < M+1 ; i++){
        dp[i][2] = i + 1;
    }
    for(int j = 3 ; j < N+1 ; j++){
        for(int i = 0 ; i < M+1 ; i++){
            for(int k = 0 ; k < i+1 ; k++){
                dp[i][j] = (dp[i][j] + dp[i-k][j-1]) % DIV_NUM;
            }
        }
    }

    cout << dp[M][N] << "\n";
    return 0;
}