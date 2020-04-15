#include <iostream>
#include <algorithm>
#define MAX_NUM 100000
using namespace std;

int M, ans, arr[MAX_NUM], dp[MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    ans = dp[0] = arr[0];

    for(int i = 1 ; i < M ; i++){
        dp[i] = max(arr[i], dp[i-1] + arr[i]);
        ans = max(ans, dp[i]);
    }
    
    cout << ans << "\n";
    return 0;
}

// dp[N] => N 번 째 원소를 마지막 원소로 썼을 때 Ans

// #include <iostream>

// using namespace std;
// int M, ans;
// int arr[100000];
// int dp[100000];
// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cin >> M;
//     for(int i = 0 ; i < M ; i++){
//         cin >> arr[i];
//     }

//     ans = dp[0] = arr[0];

//     for(int i = 1 ; i < M ; i++){
//         dp[i] = max(dp[i-1] + arr[i], arr[i]);
//         ans = max(ans, dp[i]);
//     }

//     cout << ans << "\n";
//     return 0;
// }