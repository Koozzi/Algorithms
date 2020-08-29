#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int sum, arr[9];

void func(int idx){
    if(sum == 100 && v.size() == 7){
        for(int i = 0 ; i < 7 ; i++){
            cout << v[i] << "\n";
        }
        exit(0);
    }
    for(int i = idx + 1 ; i < 9 ; i++){
        v.push_back(arr[i]);
        sum += arr[i];
        func(i);
        sum -= arr[i];
        v.pop_back();
    }
}

int main(){
    for(int i = 0 ; i < 9 ; i ++){
        cin >> arr[i];
    } sort(arr, arr+9);
    func(-1);
    return 0;
}