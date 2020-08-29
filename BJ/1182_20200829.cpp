#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, S, arr[20], ans, num, sum;

void func(int start){
    if(sum == S){
        ans++;
    }
    for(int i = start + 1 ; i < N ; i++){
        sum += arr[i];
        func(i);
        sum -= arr[i];
    }
}

int main(){
    cin >> N >> S;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    for(int i = 0 ; i < N ; i++){
        sum += arr[i];
        func(i);
        sum -= arr[i];
    }
    cout << ans << "\n";
    return 0;
}