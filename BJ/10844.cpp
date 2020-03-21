#include <iostream>
#include <algorithm>

#define MAX_NUM 1000000000
using namespace std;

int M, ans = 0;
int dp[101][10];

int main(){
    int sum = 0;
    cin >> M;
    dp[2][9] = 1;
    for(int i = 1 ; i <= 9 ; i++){
        dp[1][i] = 1;
    }
    for(int i = 1 ; i < 9 ; i++){
        dp[2][i] = 2;
    }
    for(int i = 3 ; i <= M ; i++){
        for(int j = 1 ; j <= 9 ; j++){
            if(j == 1){
                dp[i][j] = (dp[i-2][1] + dp[i-1][2]) % MAX_NUM;
            }
            else if(j == 9){
                dp[i][j] = (dp[i-1][8]) % MAX_NUM;
            }
            else{
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MAX_NUM;
            }
        }
    }
    for(int i = 1 ; i <= 9 ; i++){
        sum = (sum + dp[M][i]) % MAX_NUM;
    }
    cout << sum << endl;
    return 0;
}