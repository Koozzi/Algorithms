#include <algorithm>
#include <iostream>
using namespace std;

int N, arr[100000], dp[100000], ans;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    dp[0] = arr[0];
    ans = dp[0];
    for(int i = 1 ; i < N ; i++){
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}