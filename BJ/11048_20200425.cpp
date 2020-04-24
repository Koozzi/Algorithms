#include <iostream>
#include <algorithm>
using namespace std;

int M, N;
int arr[1000][1000];
int dp[1000][1000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> arr[i][j];
        }
    }

    dp[0][0] = arr[0][0];
    for(int i = 1 ; i < M ; i++){
        dp[i][0] = dp[i-1][0] + arr[i][0];
    }
    for(int i = 1 ; i < N ; i++){
        dp[0][i] = dp[0][i-1] + arr[0][i];
    }

    for(int i = 1 ; i < M ; i++){
        for(int j = 1 ; j < N ; j++){
            dp[i][j] = max(dp[i-1][j-1], max(dp[i-1][j], dp[i][j-1])) + arr[i][j];
        }
    }

    cout << dp[M-1][N-1] << "\n";
    return 0;
}