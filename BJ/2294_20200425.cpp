#include <iostream>
#include <algorithm>
using namespace std;

int M, K;
int arr[101];
int dp[10001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> M >> K;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }sort(arr, arr+M);
    
    for(int i = 1 ; i <= K ; i++){
        int MIN_NUM = 98765432;
        for(int j = 1 ; j <= M ; j++){
            if(i >= arr[j]){
                MIN_NUM = min(MIN_NUM, dp[i-arr[j]]);
            }
        }
        dp[i] = MIN_NUM + 1;
    }

    if(dp[K] == 98765433){
        cout << -1 << "\n";
        return 0;
    }
    cout << dp[K] << "\n";
    return 0;
}