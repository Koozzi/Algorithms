#include <iostream>
#define DIV_NUM 1000000000
using namespace std;

int M;
long long dp[101][10], ans;

int main(){
    cin >> M;
    for(int i = 1 ; i < 10 ; i++){
        dp[1][i] = 1;
        ans++;
    }
    for(int i = 2 ; i < M+1 ; i++){
        ans = 0;
        for(int k = 0 ; k < 10 ; k++){
            if(k != 0 && k != 9){
                dp[i][k] = (dp[i-1][k-1] + dp[i-1][k+1]) % DIV_NUM;
            }
            if(k == 0){
                dp[i][k] = dp[i-1][1];
            }
            if(k == 9){
                dp[i][k] = dp[i-1][8];
            }
            ans = (ans + dp[i][k] % DIV_NUM);
        }
    }
    cout << ans << "\n";
    return 0;
}