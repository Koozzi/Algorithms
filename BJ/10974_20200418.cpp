#include <iostream>
#include <algorithm>
using namespace std;

int M, arr[8];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        arr[i] = i + 1;
        cout << i + 1 << " ";
    }cout << "\n";
    while(next_permutation(arr, arr+M)){
        for(int i = 0 ; i < M ; i++){
            cout << arr[i] << " ";
        }cout << "\n";
    }
    return 0;
}