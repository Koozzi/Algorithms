#include <iostream>
#include <algorithm>
using namespace std;

int M, sv, mv;
int arr[101];
bool dp[101][1001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> sv >> mv;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }
    dp[0][sv] = true;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j <= mv ; j++){
            if(dp[i][j]){
                if(j - arr[i+1] >= 0){
                    dp[i+1][j-arr[i+1]] = true;
                }
                if(j + arr[i+1] <= mv){
                    dp[i+1][j+arr[i+1]] = true;
                }
            }
        }
    }

    int ans = -1;
    for(int i = 0 ; i <= mv ; i++){
        if(dp[M][i]){
            ans = i;
        }
    }

    cout << ans << "\n";
    return 0;
}