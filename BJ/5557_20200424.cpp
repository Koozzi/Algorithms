#include <iostream>
#include <algorithm>
using namespace std;

int M;
int arr[101];
int dp[101][21];

void show(){
    cout << "\n";
    for(int i = 1 ; i <= M ; i++){
        for(int j = 0 ; j <= 20 ; j++){
            cout << dp[i][j] << " ";
        }cout << "\n";
    }
}

int main(){
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }    

    dp[1][arr[1]] = 1;

    for(int i = 1 ; i <= M-2 ; i++){
        int val = arr[i+1];
        for(int j = 0 ; j <= 20 ; j++){
            if(dp[i][j] != 0){
                if(j + val <= 20){
                    dp[i+1][j+val] += dp[i][j];
                }
                if(j - val >= 0){
                    dp[i+1][j-val] += dp[i][j];
                }
            }
        }
    }
    show();
    cout << dp[M-1][arr[M]] << "\n";
    return 0;
}