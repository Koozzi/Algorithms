#include <iostream>
#include <cstring>
using namespace std;

int M, N, K;

int dp[15][15];

int route(int startI, int startJ, int endI, int endJ){
    memset(dp, 0, sizeof(dp));
    for(int i = startI ; i <= endI ; i++){
        dp[i][startJ] = 1;
    }
    for(int j = startJ ; j <= endJ ; j++){
        dp[startI][j] = 1;
    }
    for(int i = startI + 1 ; i <= endI ; i++){
        for(int j = startJ + 1 ; j <= endJ ; j++){
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    return dp[endI][endJ];    
}

int main(){
    cin >> M >> N >> K;
    if(K == 0){
        cout << route(0,0,M-1,N-1) << endl;
    }
    else{
        int I;
        int J;
        if(K % N == 0){
            I = K / N - 1;
            J = N - 1;
        }
        else{
            I = K / N;
            J = K % N - 1;
        }
        cout << route(0,0,I,J) * route(I,J,M-1,N-1) << endl;
    }
    return 0;
}