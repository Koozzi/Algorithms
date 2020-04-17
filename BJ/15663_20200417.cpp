#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

int M, N;
int arr[8];
bool used[8];

set<string> s;
vector<int> ans;

void func(){
    if(ans.size() == N){
        string str = "";
        for(int i = 0 ; i < ans.size() ; i++){
            str.push_back(ans[i] + '0');
        }
        if(s.count(str) == 0){
            for(int i = 0 ; i < ans.size() ; i++){
                cout << ans[i] << " ";
            }cout << "\n";
            s.insert(str);
        }
        return;
    }
    for(int i = 0 ; i < M ; i++){
        if(!used[i]){
            ans.push_back(arr[i]);
            used[i] = true;
            func();
            ans.pop_back();
            used[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    
    sort(arr, arr+M);
    func();
    return 0;
}