#include <iostream>
#define MAX_NUM 1000001
using namespace std;

int dp[MAX_NUM];
int M;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;

    for(int i = M - 1 ; i > 0 ; i--){
        if(i * 2 > M){
            dp[i] = dp[i+1] + 1;
        }
        else if(i * 3 > M && i * 2 <= M){
            dp[i] = min(dp[i+1], dp[i*2]) + 1;
        }
        else{
            dp[i] = min(dp[i+1], min(dp[i*2], dp[i*3])) + 1;
        }
    }
    cout << dp[1] << "\n";
    return 0;
}