#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int sum, arr[9];
vector<int> v;

void func(int start){
    if(v.size() == 7 && sum == 100){
        for(int i = 0 ; i < 7 ; i++){
            cout << v[i] << "\n";
        }
        exit(0);
    }
    for(int i = start + 1 ; i < 9 ; i++){
        sum += arr[i];
        v.push_back(arr[i]);
        func(i);
        sum -= arr[i];
        v.pop_back();
    }
}

int main(){
    for(int i = 0 ; i < 9 ; i++){
        int a; cin >> a;
        arr[i] = a;
    }sort(arr, arr+9);
    func(-1);
}