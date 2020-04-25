#include <iostream>
#include <algorithm>
#define INF 98765432;
using namespace std;

int T, M, a;

int sum[501];
int dp[501][501];

int DP(){
    for(int k = 1 ; k < M ; k++){ // k : 길이
        for(int i = 1 ; i <= M-k ; i++){
            dp[i][i+k] = INF;
            for(int j = i = i ; j < i+k ; j++){
                dp[i][i+k] = min(dp[i][i+k], dp[i][j] + dp[j+1][i+k]);
            }
            dp[i][i+k] += sum[i+k] - sum[i-1];
        }
    }
    return dp[1][M];
}

int main(){
    cin >> T;
    while(T--){
        cin >> M;
        for(int i = 1 ; i <= M ; i++){
            cin >> a;
            sum[i] = sum[i-1] + a;
        }
        cout << DP() << "\n";
    }
    return 0;
}