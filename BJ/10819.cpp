#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int M, maxAns = 0;
int arr[9];
bool visited[9];

vector<int> ans;

int getSum(){
    int a = 0;
    for(int i = 0 ; i < M - 1 ; i++){
        a += abs(ans[i] - ans[i+1]);
    }
    return a;
}

void solve(){
    if(ans.size() == M){
        maxAns = max(maxAns, getSum());
        return;
    }
    for(int i = 0 ; i < M ; i++){
        if(!visited[i]){
            ans.push_back(arr[i]);
            visited[i] = true;
            solve();
            ans.pop_back();
            visited[i] = false;
        }
    }
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    for(int i = 0 ; i < M ; i++){
        ans.push_back(arr[i]);
        visited[i] = true;
        solve();
        ans.pop_back();
        visited[i] = false;
    }
    cout << maxAns << "\n";
    return 0;
}

/*
6
20 1 15 8 4 10
-> 62
*/