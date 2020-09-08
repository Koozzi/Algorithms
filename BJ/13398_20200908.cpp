#include <algorithm>
#include <iostream>
using namespace std;

int N, ans;
int arr[100000];
int dp[100000][2];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    ans = dp[0][0] = arr[0];
    for(int i = 1 ; i < N ; i++){
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i]);
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }
    cout << ans << "\n";
    return 0;
}