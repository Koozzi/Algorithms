#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N, arr[1000];

vector<int> v;
vector<pair<int, int>> ans;
stack<int> s;

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }   

    v.push_back(arr[0]);
    ans.push_back({arr[0], 0});

    for(int i = 1 ; i < N ; i++){
        if(v.back() < arr[i]){
            ans.push_back({arr[i], v.size()});
            v.push_back(arr[i]);
        }
        else{
            auto iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter - v.begin()] = arr[i];
            ans.push_back({arr[i], iter - v.begin()});
        }
    }

    int num = v.size() - 1;
    for(int i = N - 1 ; i >= 0 ; i--){
        if(ans[i].second == num){
            s.push(ans[i].first);
            num --;
        }
    }
    cout << v.size() << "\n";
    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }

    return 0;
}