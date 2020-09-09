#include <iostream>
#include <algorithm>
using namespace std;

int N, ans, arr[100000], dp[100000][2];

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    
    ans = max(dp[0][1], dp[0][0]);

    for(int i = 1 ; i < N ; i++){
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0]);
        ans = max(ans, max(dp[i][1], dp[i][0]));
    }

    cout << ans << "\n";
    return 0;
}

/*

dp[N][0] : 원소를 삭제하지 않고 구한 최대 연속합
dp[N][1] : 원소를 하나 삭제하고 구한 최대 연속합

dp[N][0] = max(dp[i-1][0] + arr[i], arr[i]);
dp[N][1] = max(dp[i-1][1] + arr[i], dp[i-1][0]);
dp[i-1][1] + arr[i] -> 원소를 하나 삭제하고 i-1번째 원소까지 고려해서 구한 최대 연속합 + arr[i]

*/