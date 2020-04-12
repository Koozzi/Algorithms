#include <iostream>

using namespace std;
int M, ans;
int arr[100000];
int dp[100000];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    ans = dp[0] = arr[0];

    for(int i = 1 ; i < M ; i++){
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}