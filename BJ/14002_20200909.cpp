#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N, arr[1000];
stack<int> s;
vector<int> v;
vector<pair<int, int>> ans;

int main(){
    cin >> N;
    int a; cin >> a;
    v.push_back(a);
    ans.push_back({a, 0});
    for(int i = 1 ; i < N ; i++){
        cin >> a;
        if(v.back() < a){
            ans.push_back({a, v.size()});
            v.push_back(a);
        }
        else{
            auto iter = lower_bound(v.begin(), v.end(), a);
            v[iter - v.begin()] = a;
            ans.push_back({a, iter-v.begin()});
        }
    }

    int num = v.size() - 1;
    for(int i = ans.size()-1 ; i >= 0 ; i--){
        if(ans[i].second == num){
            s.push(ans[i].first);
            num--;
        }
    }
    cout << v.size() << "\n";
    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    } 
}
