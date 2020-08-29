#include <iostream>
#include <algorithm>
#define MAX_NUM 10001
using namespace std;

int arr[MAX_NUM], N;

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    if(prev_permutation(arr, arr+N)){
        for(int i = 0 ; i < N ; i++){
            cout << arr[i] << " ";
        }cout << "\n";
    }
    else{
        cout << -1 << "\n";
    }
    return 0;
}