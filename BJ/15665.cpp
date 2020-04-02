#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int M, N, startI;
bool used[8];

vector<int> arr;
vector<int> v;
set<string> ans;

void func(){
    if(v.size() == N){
        string newstr = "";
        for(int i = 0 ; i < v.size() ; i++){
            newstr.push_back(v[i] + 48);
        }
        if(ans.count(newstr) == 0){
            ans.insert(newstr);
            for(int i = 0 ; i < v.size() ; i++){
                cout << v[i] << " ";
            }
            cout << "\n";
        }
        return;
    }
    for(int i = 0 ; i < arr.size() ; i++){
        v.push_back(arr[i]);
        func();
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end());
    for(int i = 0 ; i < arr.size() ; i++){
        v.push_back(arr[i]);
        func();
        v.pop_back();
    }
    return 0;
}
