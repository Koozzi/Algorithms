#include <iostream>
#include <algorithm>
using namespace std;

int M;
long long int arr[100][100];
long long int dp[100][100];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> arr[i][j];
        }
    }

    dp[0][0] = 1;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            if(i != M-1 || j != M-1){
                if(i + arr[i][j] < M){
                    dp[i+arr[i][j]][j] += dp[i][j];
                }
                if(j + arr[i][j] < M){
                    dp[i][j+arr[i][j]] += dp[i][j];
                }
            }
        }
    }

    cout << dp[M-1][M-1] << "\n";
    return 0;
}