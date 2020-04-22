#include <iostream>
#include <algorithm>
#define MAX_NUM 1001
using namespace std;

int M, dp[MAX_NUM], arr[MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 1 ; i < M+1 ; i++){
        cin >> arr[i];
    }

    dp[1] = arr[1];
    for(int i = 2 ; i <= M ; i++){
        dp[i] = arr[i];
        for(int j = 1 ; j < i ; j++){
            dp[i] = min(dp[i], dp[i-j] + arr[j]);
        }
    }

    cout << dp[M] << "\n";
    return 0;
}