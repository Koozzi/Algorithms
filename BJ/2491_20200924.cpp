#include <iostream>
#include <algorithm>
using namespace std;

int N, max_i, max_d, arr[100000];
int increase_dp[100000];
int decrease_dp[100000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    max_i = increase_dp[0] = 1;
    for(int i = 1 ; i < N ; i++){
        if(arr[i-1] <= arr[i]){
            increase_dp[i] = increase_dp[i-1] + 1;
        }
        else{
            increase_dp[i] = 1;
        }
        max_i = max(max_i, increase_dp[i]);
    }

    max_d = decrease_dp[0] = 1;
    for(int i = 1 ; i < N ; i++){
        if(arr[i-1] >= arr[i]){
            decrease_dp[i] = decrease_dp[i-1] + 1;
        }
        else{
            decrease_dp[i] = 1;
        }
        max_d = max(max_d, decrease_dp[i]);
    }

    if(max_i > max_d) cout << max_i << "\n";
    else cout << max_d << "\n";

    return 0;
}