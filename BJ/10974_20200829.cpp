#include <iostream>
#include <algorithm>

using namespace std;

int arr[8];

void init_arr(){
    arr[0] = 1;
    for(int i = 1 ; i < 8 ; i++){
        arr[i] = arr[i-1] + 1;
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    init_arr();
    int N; cin >> N;
    for(int i = 0 ; i < N ; i++){
        cout << arr[i] << " ";
    }cout  << "\n";
    while(next_permutation(arr, arr+N)){
        for(int i = 0 ; i < N ; i++){
            cout << arr[i] << " ";
        }cout << "\n";
    }
}