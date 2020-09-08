#include <iostream>
#include <algorithm>
using namespace std;
int N, arr[1001], dp[1001];

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    dp[0] = arr[0];
    dp[1] = (arr[1] > arr[0]) ? (arr[0] + arr[1]) : arr[1];

    for(int i = 2 ; i < N ; i++){
        dp[i] = arr[i];
        for(int j = 0 ; j < i ; j++){
            if(arr[j] < arr[i]){
                dp[i] = max(dp[i], dp[j] + arr[i]);
            }
        }
    }

    int ans = 0;
    for(int i = 0 ; i < N ; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}