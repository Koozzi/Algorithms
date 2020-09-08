#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N, arr[1000];
vector<int> v;
int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    v.push_back(arr[N-1]);
    for(int i = N - 2 ; i >= 0 ; i--){
        if(v.back() < arr[i]){
            v.push_back(arr[i]);
        }
        else{
            auto iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter - v.begin()] = arr[i];
        }
    }
    cout << v.size() << "\n";
    return 0;
}