#include <iostream>

using namespace std;

long long int M;
long long int dp[1001];

int main(){
    cin >> M;
    
    dp[1] = 1;
    dp[2] = 2;

    for(int i = 3 ; i <= M ; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;
    }

    cout << dp[M] << "\n";
    return 0;
}