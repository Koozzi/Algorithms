#include <iostream>
#include <algorithm>
#define MAX_NUM 100001
using namespace std;

int T, M;
int arr[2][MAX_NUM];
int dp[2][MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    while(T--){
        cin >> M;
        for(int i = 0 ; i < 2 ; i++){
            for(int k = 1 ; k < M+1 ; k++){
                cin >> arr[i][k];
            }
        }
        
        dp[0][1] = arr[0][1];
        dp[1][1] = arr[1][1];
        dp[0][2] = arr[1][1] + arr[0][2];
        dp[1][2] = arr[0][1] + arr[1][2];

        for(int i = 3 ; i < M+1 ; i++){
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i];
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i];
        }

        for(int i = 0 ; i < 2 ; i++){
            for(int j = 1 ; j < M+1 ; j++){
                cout << dp[i][j] << " ";
            }cout << "\n";
        }

        cout << max(dp[0][M], dp[1][M]) << "\n";
    }
    return 0;
}