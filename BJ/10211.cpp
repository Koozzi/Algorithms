#include <iostream>

using namespace std;
int T, M, ans;
int arr[1000];
int dp[1000];

int main(){
    cin >> T;
    while(T--){
        cin >> M;
        for(int i = 0 ; i < M ; i++){
            cin >> arr[i];
        }
        dp[0] = arr[0];
        ans = dp[0];
        for(int i = 1 ; i < M ; i++){
            dp[i] = max(dp[i-1] + arr[i], arr[i]);
            ans = max(ans, dp[i]);
        }
        cout << ans << endl;
    }
    return 0;
}

/*
4
-100 1 -2 5
-> 5

4
-100 6 -2 7
-> 11

4
1 2 3 4
-> 10

5
2 1 -2 3 -5
-> 4

5
-1 -2 -3 -4 -5
-> -1

*/