#include <algorithm>
#include <iostream>
using namespace std;

int N, M;
int arr[100000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr+N);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        if(binary_search(arr, arr+N, a)) cout << 1 << "\n";
        else cout << 0 << "\n";
    }
    return 0;
}