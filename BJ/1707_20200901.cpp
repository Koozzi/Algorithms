#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

int N, M, T;
int check[20001];
bool bipartite = true;
vector<int> v[20001];

void init_set(){
    bipartite = true;
    for(int i = 0 ; i <= N ; i++){
        v[i].clear();
        check[i] = 0;
    }
}

void BFS(int start){
    queue<int> q;
    q.push(start);
    check[start] = 1;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(check[n] == 0){
                q.push(n);
                check[n] = check[c] * -1;
            }
            else{
                if(check[c] == check[n]){
                    bipartite = false;
                    return;
                }
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--){
        cin >> N >> M;
        for(int i = 0 ; i < M ; i++){
            int a, b;
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        for(int i = 1 ; i <= N ; i++){
            if(check[i] == 0){
                BFS(i);
                if(!bipartite) break;
            }
        }
        if(bipartite)
            cout << "YES" << "\n";
        else
            cout << "NO" << "\n";
        init_set();
    }
}