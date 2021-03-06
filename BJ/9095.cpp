#include <iostream>

using namespace std;

int T, M;
int dp[11];
int main(){
    cin >> T;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    while(T--){
        cin >> M;
        for(int i = 4 ; i <= M ; i++){
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
        }
        cout << dp[M] << "\n";
    }
    return 0;
}