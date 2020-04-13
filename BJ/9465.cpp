#include <iostream>
#include <algorithm>

using namespace std;

int T, M;
int map[2][100001];
int dp[2][100001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--){
        cin >> M;
        for(int i = 0 ; i < 2 ; i++){
            for(int j = 0 ; j < M ; j++){
                cin >> map[i][j];
            }
        }

        dp[0][0] = map[0][0];
        dp[1][0] = map[1][0];

        dp[0][1] = dp[1][0] + map[0][1];
        dp[1][1] = dp[0][0] + map[1][1];

        for(int i = 2 ; i < M ; i++){
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + map[0][i];
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + map[1][i];
        }

        cout << max(dp[0][M-1] ,dp[1][M-1]) << "\n";
    }
    return 0;
}