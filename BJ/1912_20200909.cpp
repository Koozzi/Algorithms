#include <iostream>
#include <algorithm>
using namespace std;

int N, ans, arr[100000], dp[100000];

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    ans = dp[0] = arr[0];
    for(int i = 1; i < N ; i++){
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}