// #include <iostream>
// #include <algorithm>

// using namespace std;

// int M;
// int arr[10001];
// int dp[10001];

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cout.tie(0);

//     cin >> M;
//     for(int i = 1 ; i <= M ; i++){
//         cin >> arr[i];
//     }

//     dp[1] = arr[1];
//     dp[2] = arr[1] + arr[2];

//     for(int i = 3 ; i <= M ; i++){
//         dp[i] = max(dp[i-1], max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]));
//     }

//     cout << dp[M] << "\n";
//     return 0;
// }


#include <iostream>
#include <algorithm>

using namespace std;

int M;
int arr[10001];
int dp[10001][2];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }
    dp[1][1] = arr[1];
    for(int i = 2 ; i <= M ; i++){
        dp[i][0] = dp[i-1][1];
        dp[i][1] = max(dp[i-2][1], dp[i-2][0] + arr[i-1]) + arr[i];
    }
    cout << max(dp[M][0], dp[M][1]) << "\n";
    return 0;
}