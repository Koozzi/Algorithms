#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, N;
int arr[8];

vector<int> ans;

void func(int start){
    if(ans.size() == N){
        for(int i = 0 ; i < ans.size() ; i++){
            cout << ans[i] << " ";
        }cout << "\n";
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
    }

    sort(arr, arr+M);

    for(int i = 0 ; i < M ; i++){
        ans.push_back(arr[i]);
        func(i);
        ans.pop_back();
    }
}
