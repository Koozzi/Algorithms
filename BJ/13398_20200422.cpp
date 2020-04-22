#include <iostream>
#include <algorithm>
#define MAX_NUM 100000
using namespace std;

int M, ans, dp[MAX_NUM][2], arr[MAX_NUM];

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    
    dp[0][0] = arr[0];
    ans = max(dp[0][1], dp[0][0]);

    for(int i = 1 ; i < M ; i++){
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i]);
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }

    cout << ans << "\n";
    return 0;
}