#include <iostream>
using namespace std;

int M, t[16], p[16], dp[16];

int main(){
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> t[i] >> p[i];
    }

    if(t[M] == 1) dp[M] = p[M];

    for(int i = M-1 ; i >= 0 ; i--){
        if(t[i] + i  > M + 1){
            dp[i] = dp[i+1];
            continue;
        }
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i]);
    }
    
    cout << dp[1] << "\n";
    
    return 0;
}