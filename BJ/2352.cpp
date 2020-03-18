#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M;
int arr[40001];

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
    cout << ans.size() << endl;
    return 0;
}

/*
6
4 2 6 3 1 5
-> 3

5
4 5 1 2 3
-> 3

7
1 2 6 7 3 4 5
-> 5

6
3 4 5 1 2 6
-> 4
*/