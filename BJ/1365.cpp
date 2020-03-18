#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M;
int arr[100001];

vector<int> ans;

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    ans.push_back(arr[0]);
    for(int i = 1 ; i < M ; i++){
        if(arr[i] > ans.back()){
            ans.push_back(arr[i]);
        }
        else{
            vector<int>::iterator iter = lower_bound(ans.begin(), ans.end(), arr[i]);
            ans[iter - ans.begin()] = arr[i];
        }
    }
    cout <<  M - ans.size() << endl;
    return 0;
}