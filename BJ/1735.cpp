#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>
#define MAX_NUM 217400000
using namespace std;

int V, E, startNode, u, v, w;
int dist[20001];

vector<pair<int, int>> relation[20001];

void BFS(){
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > pq;
    pq.push(make_pair(0, startNode));
    dist[startNode] = 0;
    while(!pq.empty()){
        int currentWeight = pq.top().first;
        int currentNode = pq.top().second;
        pq.pop();
        for(int i = 0 ; i < relation[currentNode].size() ; i++){
            int nextNode = relation[currentNode][i].first;
            int nextWeihgt = relation[currentNode][i].second;
            if(currentWeight + nextWeihgt < dist[nextNode]){
                dist[nextNode] = currentWeight + nextWeihgt;
                pq.push(make_pair(dist[nextNode], nextNode));
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> V >> E >> startNode;
    for(int i = 1 ; i <= V ; i++){
        dist[i] = MAX_NUM;
    }
    for(int i = 0 ; i < E ; i++){
        cin >> u >> v >> w;
        relation[u].push_back(make_pair(v,w));
    }
    BFS();
    for(int i = 1 ; i <= V ; i++){
        if(dist[i] == MAX_NUM){
            cout << "INF" << endl;
            continue;
        }
        cout << dist[i] << endl;
    }
    return 0;
}