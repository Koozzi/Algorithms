#include <iostream>
#include <vector>

using namespace std;

int M, N;

vector<int> ans;

void func(){
    if(ans.size() == N){
        for(int i = 0 ; i < ans.size() ; i++){
            cout << ans[i] << " ";
        }cout << "\n";
        return;
    }

    for(int i = 1 ; i <= M ; i++){
        ans.push_back(i);
        func();
        ans.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >>  M >> N;

    func();

    return 0;
}