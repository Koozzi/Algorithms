#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int M, N;
bool visited[2001];
vector<int> v[2001];

void BFS(int start){
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    q.push(make_pair(start, 0));
    visited[start] = true;
    while(!q.empty()){
        int c = q.front().first;
        int d = q.front().second;
        q.pop();

        if(d >= 4){
            cout << 1 << "\n";
            exit(0);
        }

        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(!visited[n]){
                q.push(make_pair(n, d + 1));
                visited[n] = true;
            }
        }
    }
}
int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i = 0 ; i < M ; i++){
        BFS(i);
    }

    cout << 0 << "\n";

    return 0;
}