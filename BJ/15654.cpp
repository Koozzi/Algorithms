#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;
vector<int> v;

int M, N;
bool used[10001];

void func(){
    if(v.size() == N){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = 0 ; i < M ; i++){
        if(!used[arr[i]]){
            v.push_back(arr[i]);
            used[arr[i]] = true;
            func();
            v.pop_back();
            used[arr[i]] = false;
        }
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

    func();

    return 0;
}