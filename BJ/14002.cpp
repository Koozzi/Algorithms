#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int M;
int arr[1000];

vector<int> v;
vector<pair<int, int>> ans;

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }

    v.push_back(arr[0]);
    ans.push_back(make_pair(0, arr[0]));

    for(int i = 1 ; i < M ; i++){
        if(v.back() < arr[i]){
            ans.push_back(make_pair(v.size(), arr[i]));
            v.push_back(arr[i]);
        }
        else{
            vector<int>::iterator iter = lower_bound(v.begin(), v.end(), arr[i]);
            v[iter - v.begin()] = arr[i];
            ans.push_back(make_pair(iter-v.begin(), arr[i]));
        }
    }

    // for(int i = 0 ; i < ans.size() ; i++){
    //     cout << ans[i].first << " ";
    // }cout << "\n";
    cout << v.size() << "\n";

    stack<int> s;

    int num = v.size() - 1;
    for(int i = M - 1 ; i >= 0 ; i--){
        if(ans[i].first == num){
            s.push(ans[i].second);
            num--;
        }
    }

    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }cout << "\n";

    return 0;
}