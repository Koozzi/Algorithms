#include <iostream>
#include <algorithm>

using namespace std;

int M;
int arr[10000];

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    if(next_permutation(arr, arr+M)){
        for(int i = 0 ; i < M ; i++){
            cout << arr[i] << " ";
        }cout << "\n";
    }
    else{
        cout << -1 << "\n";
    }
}

// #include <iostream>
// #include <algorithm>

// using namespace std;

// int M;
// int arr[10001];

// int main(){
//     cin >> M;

//     for(int i = 0 ; i < M ; i++){
//         cin >> arr[i];
//     }

//     if(next_permutation(arr, arr+M)){
//         for(int i = 0 ; i < M ; i++){
//             cout << arr[i] << " ";
//         }
//     }
//     else{
//         cout << -1 << "\n";
//     }

//     return 0;
// }