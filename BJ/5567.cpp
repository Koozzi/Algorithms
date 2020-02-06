#include <iostream>
#include <queue>
#include <vector>

std::vector<int> relation[10001];
bool visited[501];
int depth[501] = {0};
int invite_count = 0;
using namespace std;

int n, k;

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int current = q.front();
        if(depth[current] == 2){
            break;
        }
        q.pop();
        for(int i = 0 ; i < relation[current].size() ; i++){
            int next = relation[current][i];
            if(!visited[next]){
                visited[next] = true;
                q.push(next);
                depth[next] = depth[current] + 1;
                if (depth[next] <= 2){
                    invite_count++;
                }
            }
        }
    }
}

int main(){
    cin >> n >> k;
    for(int i = 0 ; i < k ; i++){
        int a, b;
        cin >> a >> b;
        relation[a].push_back(b);
        relation[b].push_back(a);
    }
    BFS(1);
    cout << invite_count << "\n";
    return 0;
}
