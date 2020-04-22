#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int M, ans, arr[1000];

vector<int> v;
vector<int>::iterator iter;

int LIS(int idx){
    v.clear();
    v.push_back(arr[0]);
    for(int i = 1 ; i <= idx ; i++){
        if(v.back() < arr[i]){
            v.push_back(arr[i]);
        }
        else{
            iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter-v.begin()] = arr[i];
        }
    }
    return v.size();
}

int LDS(int idx){
    v.clear();
    v.push_back(arr[M-1]);
    for(int i = M-2 ; i >= idx ; i--){
        if(v.back() < arr[i]){
            v.push_back(arr[i]);
        }
        else{
            iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter-v.begin()] = arr[i];
        }
    }
    return v.size();
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    for(int i = 0 ; i < M ; i++){
        ans = max(ans, LIS(i) + LDS(i) - 1);
    }

    cout << ans << "\n";
    return 0;
}