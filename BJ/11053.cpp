#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M;
int arr[1000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    vector<int> v;
    v.push_back(arr[0]);
    for(int i = 1 ; i < M ; i++){
        if(v.back() < arr[i]) v.push_back(arr[i]);
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter - v.begin()] = arr[i];
        }
    }
    cout << v.size() << "\n";
    return 0;
}

// #include <iostream>
// #include <algorithm>
// #include <vector>

// using namespace std;

// int M;
// int arr[1000];

// vector<int> v;

// int main(){
//     cin >> M;
//     for(int i = 0 ; i < M ; i++){
//         cin >> arr[i];
//     }
//     v.push_back(arr[0]);
//     for(int i = 1 ; i < M ; i++){
//         if(arr[i] > v.back()){
//             v.push_back(arr[i]);
//         }
//         else{
//             vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
//             v[iter - v.begin()] = arr[i];
//         }
//     }
//     cout << v.size() << "\n";
//     return 0;
// }   