#include <iostream>
#include <queue>
#include <vector>
#define MAX_SIZE 101

using namespace std;
vector<int> connected[MAX_SIZE];
bool visited[MAX_SIZE];
int cnt = 0;
void bfs(int start){
    queue<int> q;
    visited[start] = true;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        int csize = connected[current].size();
        q.pop();
        for(int i = 0 ; i < csize ; i++){
            int next = connected[current][i];
            if(!visited[next]){
                cnt++;
                visited[next] = true;
                q.push(next);
            }
        }
    }
}
int main(){
    int n, k;
    cin >> n >> k;

    for(int i = 0 ; i < k ; i++){
        int a, b;
        cin >> a >> b;
        connected[a].push_back(b);
        connected[b].push_back(a);
    }
    bfs(1);
    cout << cnt << "\n";
    return 0;
}