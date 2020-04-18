#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int sum, arr[9];
vector<int> v;

void func(int start, int ans){
    if(v.size() == 7 && ans == 100){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << "\n";
        }
        exit(0);
    }
    for(int i = start + 1 ; i < 9 ; i++){
        v.push_back(arr[i]);
        sum += arr[i];
        func(i, sum);
        v.pop_back();
        sum -= arr[i];
    }
}

int main(){
    for(int i = 0 ; i < 9 ; i++){
        cin >> arr[i];
    }sort(arr, arr+9);
    func(-1, 0);
    return 0;
}