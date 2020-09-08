#include <iostream>
#include <algorithm>
using namespace std;

int dp[1000001];

int main(){
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    int N; cin >> N;
    for(int i = 4 ; i <= N ; i++){
        if(i % 2 == 0 && i % 3 == 0){
            dp[i] = min(dp[i/2], dp[i/3]) + 1;
        }
        else if(i % 2 == 0 && i % 3 != 0){
            dp[i] = min(dp[i-1], dp[i/2]) + 1;           
        }
        else if(i % 2 != 0 && i % 3 == 0){
            dp[i] = min(dp[i-1], dp[i/3]) + 1;
        }
        else{
            dp[i] = dp[i-1] + 1;
        }
    }
    cout << dp[N] << "\n";
    return 0;
}