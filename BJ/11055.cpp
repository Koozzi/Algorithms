#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int M, ans;
int arr[1000];
int dp[1000];

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    dp[0] = arr[0];

    if(arr[1] > arr[0]) dp[1] = dp[0] + arr[1];
    else dp[1] = arr[1];

    for(int i = 2 ; i < M ; i++){
        int maxDP = 0;
        for(int j = 0 ; j < i ; j++){
            if(arr[j] < arr[i]){
                maxDP = max(maxDP, dp[j]);
            }
        }
        dp[i] = maxDP + arr[i];
    }
    ans = dp[0];
    for(int i = 1 ; i < M ; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans << "\n";
    return 0;
}