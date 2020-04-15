#include <iostream>
#include <algorithm>

#define MAX_NUM 100001
using namespace std;

int M, ans, arr[MAX_NUM], dp[MAX_NUM][2];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> M;

    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }

    dp[1][0] = arr[1];
    ans = dp[1][0];

    for(int i = 2 ; i <= M ; i++){
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i]);
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }

    cout << ans << "\n";
    return 0;
}

// #include <iostream>

// using namespace std;

// int M, ans;

// int arr[100000];
// int dp[2][100000];

// int main(){
//     cin >> M;
//     for(int i = 0 ; i < M ; i++){
//         cin >> arr[i];
//     }
    
//     ans = arr[0];
//     dp[0][0] = arr[0];
    
//     for(int i = 1 ; i < M ; i++){
//         dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i]);
//         dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i]);
//         ans = max(ans, max(dp[0][i], dp[1][i]));
//     }

//     cout << ans << "\n";
//     return 0;    
// }

