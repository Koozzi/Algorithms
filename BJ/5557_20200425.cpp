#include <iostream>
#include <algorithm>
using namespace std;

int M;
long long int arr[101];
long long int dp[101][21];

long long int DP(){
    dp[1][arr[1]] = 1;

    for(int i = 1 ; i <= M-2 ; i++){
        int val = arr[i+1];
        for(int j = 0 ; j <= 20 ; j++){
            if(dp[i][j] != 0){
                if(j - val >= 0){
                    dp[i+1][j-val] += dp[i][j];
                }
                if(j + val <= 20){
                    dp[i+1][j+val] += dp[i][j];
                }
            }
        }
    }
    return dp[M-1][arr[M]];
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }

    cout << DP() << "\n";
    return 0;
}