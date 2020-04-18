#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int M, sum, ans, arr[8];

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }sort(arr, arr+M);
    for(int i = 0 ; i < M - 1; i++){
        ans += abs(arr[i] - arr[i + 1]);
    }
    while(next_permutation(arr, arr+M)){
        sum = 0;
        for(int i = 0 ; i < M - 1 ; i++){
            sum += abs(arr[i] - arr[i + 1]);
        }
        ans = max(ans, sum);
    }
    cout << ans << "\n";
    return 0;
}