#include <iostream>
using namespace std;

int M, N;
int arr[101];
int dp[10001];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }
    dp[0] = 1;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            if(j >= arr[i]){
                dp[j] += dp[j - arr[i]];
            }
        }
    }

    cout << dp[N] << "\n";
    return 0;
}