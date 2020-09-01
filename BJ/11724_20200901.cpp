#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, ans;
bool visited[1001];
vector<int> v[1001];

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int current_node = q.front();
        q.pop();
        for(int i = 0 ; i < v[current_node].size() ; i++){
            int next_node = v[current_node][i];
            if(!visited[next_node]){
                q.push(next_node);
                visited[next_node] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);       
    }
    for(int i = 1 ; i <= N ; i++){
        if(!visited[i]){
            BFS(i);
            ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}