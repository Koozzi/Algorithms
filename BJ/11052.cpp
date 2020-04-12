#include <iostream>

using namespace std;

int M;
int arr[1001];
int dp[1001];

int main(){
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }
    dp[1] = arr[1];
    for(int i = 2 ; i <= M ; i++){
        dp[i] = arr[i];
        for(int j = 1 ; j < i ; j++){
            dp[i] = max(dp[i], dp[j] + arr[i-j]);
        }
    }
    cout << dp[M] << "\n";
    return 0;
}