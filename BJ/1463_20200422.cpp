#include <iostream>
#include <algorithm>
#define INIT_NUM 98765432
#define MAX_NUM 1000001
using namespace std;

int dp[MAX_NUM]; 
int M;

void init(){
    for(int i = 0 ; i <= M ; i++){
        dp[i] = INIT_NUM;
    }
}

int main(){
    cin >> M;
    // for(int i = M-1 ; i > 0 ; i--){
    //     if(i * 2 > M){
    //         dp[i] = dp[i+1] + 1;
    //     }
    //     else if(i * 2 <= M && i * 3 > M){
    //         dp[i] = min(dp[i+1], dp[i*2]) + 1;
    //     }
    //     else if(i + 1 <= M){
    //         dp[i] = min(dp[i+1], min(dp[i*2], dp[i*3])) + 1;
    //     }
    // }

    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;

    for(int i = 4 ; i <= M ; i++){
        if(i%3 == 0 && i%2 == 0){
            dp[i] = min(dp[i/3], dp[i/2]) + 1;
        }
        else if(i%3 == 0 && i%2 != 0){
            dp[i] = min(dp[i-1], dp[i/3]) + 1;
        }
        else if(i%3 != 0 && i%2 == 0){
            dp[i] = min(dp[i-1], dp[i/2]) + 1;
        }
        else{
            dp[i] = dp[i-1] + 1;
        }
    }
    cout << dp[M] << "\n";
    return 0;
}