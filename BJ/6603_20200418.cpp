#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int M, arr[12];
vector<int> v;
void func(int start){
    if(v.size() == 6){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start + 1 ; i < M ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while(1){
        cin >> M;
        if(M == 0) break;
        for(int i = 0 ; i < M ; i++){
            cin >> arr[i];
        }
        func(-1);
        cout << "\n";
    }
    return 0;
}