#include <iostream>
#include <algorithm>
#include <vector>
#define MAX_NUM 13
using namespace std;

int N, arr[MAX_NUM];
vector<int> v;

void func(int start){
    if(v.size() == 6){
        for(int i = 0 ; i < 6 ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start + 1 ; i < N ; i++){
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
        cin >> N;
        if(N == 0) break;
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        func(-1);
        cout << "\n";
    }
    return 0;
}