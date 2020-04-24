#include <iostream>
#include <algorithm>
#define DIV_NUM 1000000007
using namespace std;

int T, M;
long long int dp[5001];

void DP(){
    dp[0] = 1;
    for(int i = 2 ; i <= 5000 ; i += 2){
        for(int j = 2 ; j <= i ; j += 2){
            dp[i] += (dp[j-2] * dp[i-j]) % DIV_NUM;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    DP();

    cin >> T;
    while(T--){
        cin >> M;
        cout << dp[M] << "\n";
    }
    return 0;
}