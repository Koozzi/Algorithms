#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, arr[1000];

vector<int> v;

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    v.push_back(arr[M-1]);
    for(int i = M-2 ; i >= 0 ; i--){
        if(v.back() < arr[i]){
            v.push_back(arr[i]);
            continue;
        }
        vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
        v[iter - v.begin()] = arr[i];
    }
    cout << v.size() << "\n";
    return 0;
}