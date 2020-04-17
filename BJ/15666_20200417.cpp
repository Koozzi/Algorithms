#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>

using namespace std;

int M, N;
int arr[8];

vector<int> ans;
set<string> s;

void func(int start){
    if(ans.size() == N){
        string str = "";
        for(int i = 0 ; i < ans.size() ; i++){
            str.push_back(ans[i] + '0');
        }
        if(s.count(str) == 0){
            s.insert(str);
            for(int i = 0 ; i < ans.size() ; i++){
                cout << ans[i] << " ";
            }cout << "\n";
        }
        return;
    }
    for(int i = start ; i < M ; i++){
        ans.push_back(arr[i]);
        func(i);
        ans.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }sort(arr, arr+M);

    for(int i = 0 ; i < M ; i++){
        ans.push_back(arr[i]);
        func(i);
        ans.pop_back();
    }
}