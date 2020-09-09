#include <iostream>
#include <algorithm>
using namespace std;

int N, ans, arr[1000], dp[1000];

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    ans = dp[0] = arr[0];
    for(int i = 1 ; i < N ; i++){
        dp[i] = arr[i];
        for(int j = 0 ; j < i ; j++){
            if(arr[j] < arr[i]){
                dp[i] = max(dp[i], dp[j] + arr[i]);
            }
        }
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}