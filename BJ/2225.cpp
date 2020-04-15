#include <iostream>
#define MAX_NUM 1000000000
using namespace std;

long long int M, K, dp[201][201];

int main(){
    cin >> M >> K;

    for(int i = 0 ; i <= K ; i++){
        dp[0][i] = 1;
    }

    for(int i = 1 ; i <= M ; i++){
        dp[i][1] = 1;
        dp[i][2] = i + 1;
    }

    for(int i = 3 ; i <= K ; i++){
        for(int j = 1 ; j <= M ; j++){
            for(int k = 0 ; k <= j ; k++){
                dp[j][i] = (dp[j][i] + dp[k][i-1]) % MAX_NUM;
            }
        }
    }

    cout << dp[M][K] << "\n";
    return 0;
}