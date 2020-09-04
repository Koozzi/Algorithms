#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, arr[1000000];
vector<int> v;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    v.push_back(arr[0]);
    for(int i = 1 ; i < N ; i++){
        if(arr[i] > v.back()){
            v.push_back(arr[i]);
            continue;
        }
        vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
        v[iter - v.begin()] = arr[i];
    }
    cout << v.size() << "\n";
    return 0;
}