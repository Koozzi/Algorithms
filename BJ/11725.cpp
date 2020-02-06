#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>

#define MAX_SIZE 100001

using namespace std;

void bfs(int start);

vector<int> connected[MAX_SIZE];
bool visited[MAX_SIZE];
int parent_num[MAX_SIZE];

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
                parent_num[next] = current;
                q.push(next);
            }
        }
    }
}

int main(){
    int n;
    cin >> n;
    for(int i = 0 ; i < n - 1 ; i++){
        int a , b;
        cin >> a >> b;
        connected[a].push_back(b);
        connected[b].push_back(a);
    }
    
    for(int i = 1 ; i < n+1 ; i++){
        if(!visited[i]){
            bfs(i);
        }
    }
    for(int i = 2 ; i < n+1 ; i++){
        printf("%d\n", parent_num[i]);
        // cout << parent_num[i] << "\n";
    }
    return 0;
}
