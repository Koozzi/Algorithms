#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int T, M;

int sum[501];
int dp[501][501];

int DP(){
    for(int k = 1 ; k < M ; k++){ // 길이 : k + 1
        for(int i = 1 ; i <= M-k ; i++){ // 시작점 : i
            dp[i][i+k] = INF; 
            for(int j = i ; j < i+k ; j++){
                dp[i][i+k] = min(dp[i][i+k], dp[i][j] + dp[j+1][i+k]);
            }
            dp[i][i+k] += sum[i+k] - sum[i-1];
        }
    }
    return dp[1][M];
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--){
        cin >> M; 
        for(int i = 1 ; i < M+1 ; i++){
            int a; cin >> a;
            sum[i] = sum[i-1] + a;
        }
        cout << DP() << "\n";
    }
    return 0;
}