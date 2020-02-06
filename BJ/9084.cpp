#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    int coin_value[21] = {0};
    for(int t = 0 ; t < T ; t++){
        int N, M;
        cin >> N;
        for(int i = 1 ; i < N+1 ; i++){
            cin >> coin_value[i];
        }
        cin >> M;

        int dp[10001] = {0};
        dp[0] = 1;

        for(int i = 1 ; i < N+1 ; i++){
            for(int j = coin_value[i] ; j < M+1 ; j++){
                dp[j] += dp[j-coin_value[i]];
            }
        }
        cout << dp[M] << "\n";
    }
    return 0;
}