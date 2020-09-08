#include <iostream>
#define DIV_NUM 1000000000
using namespace std;

long long dp[101][10];

int main(){
    int N; cin >> N;
    for(int i = 1 ; i < 10 ; i++){
        dp[1][i] = 1;
    }
    for(int i = 2 ; i <= N ; i++){
        dp[i][0] = dp[i-1][1];
        dp[i][9] = dp[i-1][8];
        for(int j = 1 ; j < 9 ; j++){
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % DIV_NUM;
        }
    }
    int sum = 0;
    for(int i = 0 ; i <= 9 ; i++){
        sum = (sum + dp[N][i]) % DIV_NUM;
    } 
    cout << sum << "\n";
    return 0;
}