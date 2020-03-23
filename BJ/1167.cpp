#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

vector<pair<int, int>> v[100001];

int M, sum, ans, a, b, c;
int newStart;
bool visited[100001];

void BFS(int startNode){
    queue<pair<int, int>> q;
    q.push(make_pair(startNode, 0));
    visited[startNode] = true;
    while(!q.empty()){
        int currentNode = q.front().first;
        int dist = q.front().second;
        if(dist >= ans){
            ans = dist;
            newStart = currentNode;
        }
        q.pop();
        for(int i = 0 ; i < v[currentNode].size() ; i++){
            int nextNode = v[currentNode][i].first;
            int distNode = dist + v[currentNode][i].second;
            if(!visited[nextNode]){
                q.push(make_pair(nextNode, distNode));
                visited[nextNode] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> a;
        while(1){ 
            cin >> b;
            if(b == -1){
                break;
            }
            cin >> c;
            v[a].push_back(make_pair(b,c));
        }
    }
    BFS(1);
    memset(visited, false, sizeof(visited));
    BFS(newStart);

    cout << ans << endl;
    return 0;
}