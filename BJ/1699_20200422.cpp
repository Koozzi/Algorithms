#include <iostream>
#include <algorithm>
#include <cmath>
#define INIT_NUM 98765432
#define MAX_NUM 100001
using namespace std;

int M, dp[MAX_NUM];

int main(){
    cin >> M;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    for(int i = 4 ; i < M+1 ; i++){
        int a = int(sqrt(i));
        if(a * a == i){
            dp[i] = 1;
            continue;
        }
        dp[i] = INIT_NUM;
        for(int j = 1 ; j * j < i ; j++){
            dp[i] = min(dp[i], dp[j*j] + dp[i-j*j]);
        }
    }

    cout << dp[M] << "\n";
    return 0;
}
