#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

int N, M;
int dp[100001];

int main(){
    cin >> N;

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;

    for(int i = 4 ; i <= N ; i++){
        int a = sqrt(i);
        if(a * a == i){
            dp[i] = 1;
            continue;
        }
        dp[i] = 2e9;
        for(int j = 1 ; j * j < i ; j++){
            dp[i] = min(dp[i], dp[j*j] + dp[i-j*j]);
        }
    }
    cout << dp[N] << "\n";
    return 0;
}