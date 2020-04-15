#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int M, N, ans;
bool visited[1001];
vector<int> v[1001];

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(!visited[n]){
                q.push(n);
                visited[n] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i = 1 ; i <= M ; i++){
        if(!visited[i]){
            ans++;
            BFS(i);
        }
    }
    cout << ans << "\n";
    return 0;
}



// #include <iostream>
// #include <queue>
// #include <vector>
// #include <stdio.h>
// #include <cstring>

// #define MAX_SIZE 1001

// using namespace std;

// void bfs(int start);

// vector<int> connected[MAX_SIZE];
// bool visited[MAX_SIZE];

// void bfs(int start){
//     queue<int> q;

//     visited[start] = true;
//     q.push(start);
//     while(!q.empty()){
//         int current = q.front();
//         q.pop();
//         int csize = connected[current].size();
//         for(int i = 0 ; i < csize ; i++){
//             int next = connected[current][i];
//             if(!visited[next]){
//                 visited[next] = true;
//                 q.push(next);
//             }
//         }
//     }
// }

// int main(){
//     int n, m;
//     cin >> n >> m;
//     for(int i = 0 ; i < m ; i++){
//         int u, v;
//         cin >> u >> v;
//         connected[u].push_back(v);
//         connected[v].push_back(u);
//     }
//     int cnt = 0;
//     memset(visited, false, sizeof(visited));
//     for(int i = 1 ; i <= n ; i++){
//         if(!visited[i]){
//             cnt++;
//             bfs(i);
//         }
//     }
//     cout << cnt << "\n";
//     return 0;
// }