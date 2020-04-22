#include <iostream>
#include <algorithm>
using namespace std;

int M, arr[1000], dp[1000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    dp[0] = arr[0];
    if(arr[1] > arr[0]){
        dp[1] = arr[0] + arr[1];
    }else{
        dp[1] = arr[1];
    }

    for(int i = 2 ; i < M ; i++){
        dp[i] = arr[i];
        for(int j = 0 ; j < i ; j++){
            if(arr[j] < arr[i]){
                dp[i] = max(dp[i], dp[j] + arr[i]);
            }
        }
    }

    int ans = 0;
    for(int i = 0 ; i < M ; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}