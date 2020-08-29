#include <iostream>
#include <algorithm>
#define MAX_NUM 8
using namespace std;

int N, ans, arr[MAX_NUM];

int get_sum(){
    int sum = 0;
    for(int i = 0 ; i < N-1 ; i++){
        sum += abs(arr[i] - arr[i+1]);
    }
    return sum;
}

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }sort(arr, arr+N);
    ans = get_sum();
    while(next_permutation(arr, arr+N)){
        ans = max(ans, get_sum());
    }
    cout << ans << "\n";
    return 0;
}