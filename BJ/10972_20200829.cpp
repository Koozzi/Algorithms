#include <iostream>
#include <algorithm>
#define MAX_NUM 10001
using namespace std;

int N, arr[MAX_NUM];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N; cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } 
    if(next_permutation(arr, arr+N)){
        for(int i = 0 ; i < N ; i++){
            cout << arr[i] << " ";
        }cout << "\n";
    }
    else{
        cout << -1 << "\n";        
    }
    return 0;
}