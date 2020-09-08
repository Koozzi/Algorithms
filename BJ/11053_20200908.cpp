#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


vector<int> v;
int N; 
int arr[1000];

int main(){    
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    v.push_back(arr[0]);
    for(int i = 1 ; i < N ; i++){
        if(v.back() < arr[i]) v.push_back(arr[i]);
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter - v.begin()] = arr[i];
        }
    }
    cout << v.size() << "\n";
}