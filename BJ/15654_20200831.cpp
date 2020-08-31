#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, arr[8];
bool used[8];
vector<int> v;

void func(){
    if(v.size() == M){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = 0 ; i < N ; i++){
        if(!used[i]){
            v.push_back(arr[i]);
            used[i] = true;
            func();
            used[i] = false;
            v.pop_back();
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }sort(arr, arr+N);
    func();
    return 0;
}