#include <iostream>
using namespace std;

int M;
int arr[100][100];
long long dp[100][100];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M;
    dp[0][0] = 1;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> arr[i][j];
            if(dp[i][j] != 0 && arr[i][j] != 0){
                int nextI = i + arr[i][j];
                int nextJ = j + arr[i][j];
                if(nextI < M && nextJ < M){
                    dp[i][nextJ] += dp[i][j];
                    dp[nextI][j] += dp[i][j];
                }
                else if(nextI < M && nextJ >= M){
                    dp[nextI][j] += dp[i][j];
                }
                else if(nextI >= M && nextJ < M){
                    dp[i][nextJ] += dp[i][j];
                }
            }
        }
    }
    cout << dp[M-1][M-1] << "\n";
    return 0;
}