#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, arr[8];
vector<int> v;

void func(int start){
    if(v.size() == M){
        for(int i = 0 ; i < M ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start ; i < N ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr + N);
    func(0);
    return 0;
}