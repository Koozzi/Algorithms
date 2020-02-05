#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    long long int dp[251] = {0};
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 3;
    for(int i = 3 ; i <= n ; i++){
        dp[i] = 2 * dp[i-2] + dp[i-1];
    }
    cout << dp[n];
    return 0;
}