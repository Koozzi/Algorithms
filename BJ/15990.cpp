#include <iostream>
#define MAX_NUM 1000000009
using namespace std;

int T, M;
long long int dp[100001][4];

int main(){
    cin >> T;
    dp[1][1] = 1;
    dp[1][2] = 0;
    dp[1][3] = 0;

    dp[2][1] = 0;
    dp[2][2] = 1;
    dp[2][3] = 0;

    dp[3][1] = 1;
    dp[3][2] = 1;
    dp[3][3] = 1;

    for(int i = 4; i <= 100000 ; i++){
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MAX_NUM;
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MAX_NUM;
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MAX_NUM;
    }
    
    while(T--){
        cin >> M;
        cout << (dp[M][1] + dp[M][2] + dp[M][3]) % MAX_NUM << endl;
    }

    return 0;
}