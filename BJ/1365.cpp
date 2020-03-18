#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, a;
int arr[100001];

vector<int> ans;

int main(){
    cin >> M >> a;
    ans.push_back(a);
    for(int i = 1 ; i < M ; i++){
        cin >> a;
        if(a > ans.back()){
            ans.push_back(a);
        }
        else{
            vector<int>::iterator iter = lower_bound(ans.begin(), ans.end(), a);
            ans[iter - ans.begin()] = a;
        }
    }
    cout <<  M - ans.size() << endl;
    return 0;
}