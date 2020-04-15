#include <iostream>
#include <cstring>
#include <cmath>
#define MAX_NUM 100001

using namespace std;

int M, tmp = 1, dp[MAX_NUM];

int main(){
    cin >> M;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    for(int i = 4 ; i <= M ; i++){
        dp[i] = MAX_NUM;
        int a = sqrt(i);
        if(a * a == i){
            dp[i] = 1;
            continue;
        }
        for(int j = 1 ; j <= a ; j++){
            dp[i] = min(dp[i], dp[j*j] + dp[i-j*j]);
        }
    }
    cout << dp[M] << "\n";
    return 0;
}