#include <iostream>
using namespace std;

int T, M;
int dp[11];

void DP(){
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i = 4 ; i < 11 ; i++){
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    }
}

int main(){
    DP();
    cin >> T;
    while(T--){
        int a; cin >> a;
        cout << dp[a] << "\n";
    }
    return 0;
}