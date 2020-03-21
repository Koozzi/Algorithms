#include <iostream>
#include <cstring>

#define MAX_NUM 1000000000
using namespace std;

int M;
long long int dp[101][10];

int main(){
    memset(dp, 0, sizeof(dp));
    
    cin >> M;
    if(M < 10){
        cout << 0 << endl;
        return 0;
    }

    if(M == 10){
        cout << 1 << endl;
        return 0;
    }

    dp[10][9] = 1;

    dp[11][1] = 1;
    dp[11][8] = 1;
    dp[11][9] = 1;
    
    for(int i = 12 ; i <= M ; i++){
        for(int j = 1 ; j <= 9 ; j++){
            if(j == 9){
                dp[i][j] = (dp[i-1][j-1]) % MAX_NUM;
            }
            else if(j == 1){
                dp[i][j] = (dp[i-2][1] + dp[i-1][2]) % MAX_NUM;
            }
            else{
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MAX_NUM;
            }
        }
    }
    long long int sum = 0;
    for(int i = 1 ; i < 10 ; i++){
        sum = (sum + dp[M][i]) % MAX_NUM;
    }
    cout << sum << endl;
    return 0;
}