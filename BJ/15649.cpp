#include <iostream>
#include <vector>

using namespace std;

int M, N;
bool used[9];

vector<int> v;

void solve(int start){
    if(v.size() == N){
        for(int i = 0 ; i < N ; i++){
            cout << v[i] << " ";
        }
        cout << "\n";
        return;
    }
    for(int i = 1 ; i <= M ; i++){
        if(!used[i]){
            v.push_back(i);
            used[i] = true;
            solve(i);
            v.pop_back();
            used[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i = 1 ; i <= M ; i++){
        v.push_back(i);
        used[i] = true;
        solve(i);
        v.pop_back();
        used[i] = false;
    }

    return 0;
}