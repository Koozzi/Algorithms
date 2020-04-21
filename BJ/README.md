#include <iostream>
#include <vector>
using namespace std;

int M, N;

vector<int> v[2001];
vector<int> ans;

void initset(){
    ios_base::sync_with_stdio(0;
    cin.tie(0);
    cout.tie(0);
}

void DFS(int curt){
    if(ans.size() == 5){
        cout << 1 << "\n";
        exit(0);
    }
    for(int i = 0 ; i < v[curt].size() ; i++){
        ans.push_back(v[curt][i]);
        DFS(v[curt][i]);
        ans.pop_back();
    }
}

int main(){
    initset();
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    DFS(-1);
    cout << 0 << "\n";
    return 0;
}
