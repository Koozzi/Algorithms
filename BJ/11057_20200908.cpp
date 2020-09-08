#include <iostream>
#define DIV_NUM 10007
using namespace std;

long long dp[1001][10];

int main(){
    int N; cin >> N;
    for(int i = 0 ; i < 10 ; i++){
        dp[1][i] = 1;
    }
    for(int i = 2 ; i <= N ; i++){
        for(int j = 0 ; j < 10 ; j++){
            for(int k = 0 ; k <= j ; k++){
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % DIV_NUM;
            }
        }
    }
    long long ans = 0;
    for(int i = 0 ; i < 10 ; i++){
        ans = (ans + dp[N][i]) % DIV_NUM;
    }
    cout << ans << "\n";
    return 0;
}