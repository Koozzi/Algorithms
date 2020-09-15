#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
long long arr[100000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr+N);

    int left = 0;
    int right = N-1;
    long long sum = arr[left] + arr[right];

    int ans_left = 0;
    int ans_right = 0;
    int min_sum = 2e9;

    while(left < right){
        if(min_sum > abs(sum)){
            min_sum = abs(sum);
            ans_left = left;
            ans_right = right;
        }
        if(sum == 0){
            cout << arr[left] << " " << arr[right] << "\n";
            return 0;
        }
        else if(sum > 0){
            sum -= arr[right--];
            sum += arr[right];
        }
        else{
            sum -= arr[left++];
            sum += arr[left];
        }
    }
    cout << arr[ans_left] << " " << arr[ans_right] << "\n";
    return 0;
}