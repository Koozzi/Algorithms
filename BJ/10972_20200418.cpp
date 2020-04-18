#include <iostream>
#include <algorithm>
using namespace std;

int M;
int arr[10000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    if(!next_permutation(arr, arr+M)){
        cout << -1 << "\n";
        return 0;
    }

    for(int i = 0 ; i < M ; i++){
        cout << arr[i] << " ";
    }cout << "\n";

    return 0;
}