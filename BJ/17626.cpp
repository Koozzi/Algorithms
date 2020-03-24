#include <iostream>

using namespace std;

int M;
int dp[50001];

int main(){
    cin >> M;
    for(int i = 1 ; i * i <= M ; i++){
        dp[i*i] = 1;
        for(int j = i*i + 1 ; j < (i+1) * (i+1) ; j++){
            int tmp = 50000;
            for(int k = i ; k >= 1 ; k--){
                tmp = min(tmp, dp[j - k*k]);
            }
            dp[j] = tmp + 1;
        }
    }
    cout << dp[M] << endl;
    return 0;
}