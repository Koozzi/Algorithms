#include <iostream>
#include <algorithm>
#define MAX_NUM 10000
using namespace std;

int M, arr[MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    if(!prev_permutation(arr, arr+M)){
        cout << -1 << "\n";
        return 0;
    }

    for(int i = 0 ; i < M ; i++){
        cout << arr[i] << " ";
    }cout << "\n";

    return 0;
}