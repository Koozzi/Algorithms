#include <iostream>
#include <algorithm>
using namespace std;

int M;
long long int dp[101];

int main(){
    cin >> M;
    for(int i = 0 ; i < 6 ; i++){
        dp[i] = i;
    }
    for(int i = 6 ; i <= M ; i++){
        dp[i] = max(dp[i-1] + 1, max(dp[i-3] * 2, max(dp[i-4] * 3, dp[i-5] * 4)));
    }
    cout << dp[M] << "\n";
    return 0;
}