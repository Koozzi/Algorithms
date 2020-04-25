#include <iostream>
#include <algorithm>
using namespace std;

int M, K;
int arr[101][2];
int dp[101][100001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> K;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i][0] >> arr[i][1];
    }

    for(int i = 0 ; i <= K ; i++){
        if(arr[1][0] <= i){
            dp[1][i] = arr[1][1];
        }
    }

    for(int i = 2 ; i <= M ; i++){
        int w = arr[i][0];
        int v = arr[i][1];
        for(int j = 1 ; j <= K ; j++){
            dp[i][j] = dp[i-1][j];
            if(w <= j){
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v);
            }
        }
    }

    cout << dp[M][K] << "\n";
    return 0;
}