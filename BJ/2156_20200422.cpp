#include <iostream>
#include <algorithm>
#define MAX_NUM 10001
using namespace std;

int M, ans, dp[MAX_NUM], arr[MAX_NUM];

int main(){
    cin >> M;
    for(int i = 1 ; i < M+1 ; i++){
        cin >> arr[i];
    }
    dp[1] = arr[1];
    dp[2] = arr[1] + arr[2];
    dp[3] = max(arr[1], arr[2]) + arr[3];

    for(int i = 4 ; i < M+1 ; i++){
        dp[i] = max(dp[i-1], max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i]);
    }

    cout << dp[M] << "\n";
    return 0;
}