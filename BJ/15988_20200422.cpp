#include <iostream>
#define MAX_NUM 1000001
#define DIV_NUM 1000000009
using namespace std;

int T, M;
long long dp[MAX_NUM];

int main(){
    cin >> T;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i = 4 ; i < MAX_NUM ; i++){
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % DIV_NUM;
        // 대략 10 억 + 10억 + 10억 하면 int의 범위 넘어감
    }
    while(T--){
        cin >> M;
        cout << dp[M] << "\n";
    }
    return 0;
}