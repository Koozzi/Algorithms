// 시간초과
#include <iostream>

using namespace std;

int N, K;
int dp[3][4000001];
int main(){
    cin >> N >> K;
    dp[1][0] = 1;
    dp[1][1] = 1;
    for(int i = 2 ; i <= N ; i++){
        for(int j = 0 ; j <= i ; j++){
            if(i % 2 == 0){
                if(j == 0 || j == i){
                    dp[2][j] = 1;
                }
                else{
                    dp[2][j] = (dp[1][j-1] + dp[1][j]) % 1000000007;
                }
            }
            else{
                if(j == 0 || j == i){
                    dp[1][j] = 1;
                }
                else{
                    dp[1][j] = (dp[2][j-1] + dp[2][j]) % 1000000007;
                }
            }
        }
    }
    if(N % 2 == 0){
        cout << dp[2][K] << endl;
    }
    else{
        cout << dp[1][K] << endl;
    }
    return 0;
}