#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N;

vector<int> arr;
vector<int> v;

void func(int start){
    if(v.size() == N){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start ; i < arr.size() ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end());

    func(0);
    return 0;
}