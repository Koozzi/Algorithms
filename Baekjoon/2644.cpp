#include <iostream>
#include <queue>
#include <vector>
#define MAX_SIZE 101

using namespace std;

vector<int> connected[MAX_SIZE];
bool visited[MAX_SIZE];
int depth[MAX_SIZE];
int cnt = -1;
int n = 0;
void bfs(int start){
    queue<int> q;
    visited[start] = true;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        int csize = connected[current].size();
        for(int i = 0 ; i < csize ; i++){
            int next = connected[current][i];
            if(!visited[next]){
                visited[next] = true;
                depth[next] = depth[current] + 1;
                q.push(next);
            }
        }
    }
}

int main(){
    int m1, m2, k;
    cin >> n >> m1 >> m2 >> k;
    for(int i = 0 ; i < k ; i++){
        int a, b;
        cin >> a >> b;
        connected[a].push_back(b);
        connected[b].push_back(a);
    }

    bfs(m1);
    if(visited[m2]){
        cout << depth[m2] << "\n";
    }
    else{
        cout << -1 << "\n";
    }
    return 0;
}