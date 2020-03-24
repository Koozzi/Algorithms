#include <iostream>
#include <string>

using namespace std;

int M, N, ans = 0;
int dp[1000][1000];
string map[1000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < map[i].size() ; j++){
            dp[i][j] = map[i][j] - 48;
            ans = max(ans, dp[i][j]);
        }
    }
    
    for(int i = 1 ; i < M ; i++){
        for(int j = 1 ; j < N ; j++){
            if(map[i][j] == '1'){
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j],  dp[i][j-1])) + 1;
                ans = max(ans, dp[i][j]);
            }
        }
    }
    
    cout << ans * ans << endl;
    return 0;
}