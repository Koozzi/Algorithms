#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[9];

vector<int> v;

void func(int start){
    if(v.size() == 7){
        int sum = 0;
        for(int i = 0 ; i < 7 ; i++) 
            sum += v[i];
        if(sum == 100){
            for(int i = 0 ; i < 7 ; i++)
                cout << v[i] << "\n";
            exit(0);
        }
        return;
    }

    for(int i = start + 1 ; i < 9 ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }
}

int main(){
    for(int i = 0 ; i < 9 ; i++){
        cin >> arr[i];
    }

    sort(arr, arr+9);

    for(int i = 0 ; i < 9 ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }

    return 0;
}