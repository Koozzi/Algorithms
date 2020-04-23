#include <iostream>
#include <algorithm>
#define MAX_NUM 100001
using namespace std;

int M, K, ans;
int arr[101][2];
int dp[101][MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> K;
    
    v.push_back({0,0});
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i][0] >> arr[i][1];
    }
    
    for(int i = 1 ; i <= K ; i++){
        if(i >= arr[1][0]){
            dp[1][i] = arr[1][1];
        }
    }

    for(int i = 2 ; i <= M ; i++){
        for(int j = 1 ; j <= K ; j++){
            dp[i][j] = dp[i-1][j];
            int weight = arr[i][0];
            int value = arr[i][1];
            if(j >= weight){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value);
                ans = max(ans, dp[i][j]);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}