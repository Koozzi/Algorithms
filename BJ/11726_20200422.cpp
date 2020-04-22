#include <iostream>
#define DIV_NUM 10007
using namespace std;

int M;
int dp[1001];

int main(){
    cin >> M;
    dp[1] = 1;
    dp[2] = 2;
    for(int i = 3 ; i <= M ; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % DIV_NUM;
    }
    cout << dp[M] << "\n";
    return 0;
}