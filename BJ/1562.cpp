#include <iostream>

using namespace std;

long long int dp[100][10];
int arr[2] = {1, -1};
int main(){
    int N;
    cin >> N;
    for(int i = 0 ; i < 10 ; i++){
        if(i == 0){
            dp[1][i] = 0;
        }
        else{
            dp[1][i] = 1;
        }
    }
    for(int i = 2 ; i <= N ; i++){
        for(int j = 0 ; j < 10 ; j++){
            for(int k = 0 ; k < 2 ; k++){
                int nextIdx = j + arr[k];
                if(nextIdx >= 0 && nextIdx > 10){
                    dp[i][j] += (dp[i-1][nextIdx] % 1000000000);
                }
            }
        }
    }
    int sum = 0;
    for(int i = 0 ; i < 10 ; i++){
        sum += (dp[N][i] % 1000000000);
    }
    cout << sum << endl;
    return 0;
}