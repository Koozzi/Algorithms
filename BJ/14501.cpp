#include <iostream>

using namespace std;

int t[17];
int p[17];
int dp[17];
int M, ans;
int main(){
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> t[i] >> p[i];
    }
    for(int i = M ; i > 0 ; i--){
        if(i + t[i] > M + 1){
            dp[i] = dp[i + 1];
            continue;
        }
        dp[i] = max(dp[i + t[i]] + p[i], dp[i + 1]);
    }
    cout << dp[1] << "\n";
    return 0;
}
// #include <iostream>
// #include <vector>

// using namespace std;

// int M, sum, ans;

// vector<pair<int, int>> v(16);

// void func(int idx){
//     if(idx > M + 1){
//         return;
//     }
//     for(int i = idx ; i <= M ; i++){
//         sum += v[i].second;
//         func(i + v[i].first);
//         if(i + v[i].first <= M + 1){
//             ans = max(ans, sum);
//         }
//         sum -= v[i].second;
//     }
// }

// int main(){
//     cin >> M;
//     for(int i = 1 ; i <= M ; i++){
//         cin >> v[i].first >> v[i].second;
//     }
//     func(1);
//     cout << ans << "\n";
//     return 0;
// }