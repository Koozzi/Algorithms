#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, a;

vector<int> ans;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
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