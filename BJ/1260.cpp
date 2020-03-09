#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <memory.h>
#include <algorithm>

using namespace std;

vector<int> relation[1001];

int N, M, startNode;
bool visited[1001];
void BFS(){
    memset(visited, false, sizeof(visited));
    queue<int> q;
    q.push(startNode);
    visited[startNode] = true;
    while(!q.empty()){
        int currentNode = q.front();
        cout << currentNode << " ";
        q.pop();
        for(int i = 0 ; i < relation[currentNode].size() ; i++){
            int nextNode = relation[currentNode][i];
            if(!visited[nextNode]){
                q.push(nextNode);
                visited[nextNode] = true;
            }            
        }  
    }
}

void DFS(int root){
    visited[root] = true;
    cout << root << " ";
    for(int i = 0 ; i < relation[root].size() ; i++){
        if(!visited[relation[root][i]]){
            DFS(relation[root][i]);
        }
    }
}

int main(){
    cin >> N >> M >> startNode;
    for(int i = 0 ; i < M ; i++){
        int a, b;
        cin >> a >> b;
        relation[a].push_back(b);
        relation[b].push_back(a);
    }
    for(int i = 0 ; i < N ; i++){
        sort(relation[i].begin(), relation[i].end());
    }
    DFS(startNode);
    cout << endl;
    BFS();
}