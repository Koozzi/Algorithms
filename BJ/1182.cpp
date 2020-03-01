#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

int M, N, cnt = 0;

vector<int> v;
vector<int> ans;

void letAdd(int start){
    int tmp = 0;
    for(int i = 0 ; i < ans.size() ; i++){
        tmp += ans[i];
    }
    if(tmp == N){
        cnt++;
    }
    for(int i = start+1 ; i < M ; i++){
        ans.push_back(v[i]);
        letAdd(i);
        ans.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    for(int i = 0 ; i < M ; i++){
        ans.push_back(v[i]);
        letAdd(i);
        ans.pop_back();
    }
    cout << cnt << "\n";
    return 0;
}