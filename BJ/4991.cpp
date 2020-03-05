#include <iostream>
#include <memory.h>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int N, M, ans = 99999;
char map[21][21];
bool visited[21][21];
bool check[11];
int Distance[11][11];

vector<pair<pair<int, int>, int>> nodeInfo;
vector<pair<pair<int, int>, int>> dist;
vector<int> v;
typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int BFS(int startI, int startJ, int endI, int endJ){
    memset(visited, false, sizeof(visited));
    int depth[21][21] = {0};
    queue<pair<int, int>> q;
    q.push(make_pair(startI, startJ));
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] != 'x'){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                    if(nextI == endI && nextJ == endJ){
                        return depth[nextI][nextJ];
                    }
                }
            }
        }
    }
    return 99999;
}
void getDistance(){
    for(int i = 0 ; i < nodeInfo.size(); i++){
        for(int j = 0 ; j < nodeInfo.size() ; j++){
            int startNode = nodeInfo[i].second; 
            int endNode = nodeInfo[j].second;
            int DD = BFS(nodeInfo[i].first.first, nodeInfo[i].first.second, nodeInfo[j].first.first, nodeInfo[j].first.second);
            if(startNode == endNode){
                Distance[startNode][endNode] = 0;    
            }
            else{
                Distance[startNode][endNode] = DD;
            }
        }
    }
}
void letsClean(int start){
    if(v.size() == nodeInfo.size()){
        int sum = 0;
        for(int i = 0 ; i < v.size() - 1 ; i++){
            sum += Distance[v[i]][v[i+1]];
        }
        ans = min(ans, sum);
        return;
    }
    else{
        for(int i = 1 ; i < nodeInfo.size() ; i++){
            if(!check[nodeInfo[i].second]){
            v.push_back(nodeInfo[i].second);
            check[nodeInfo[i].second] = true;
            letsClean(i);
            v.pop_back();
            check[nodeInfo[i].second] = false;
            }
        }
    }
}

int main(){
    while(1){
        cin >> N >> M;
        ans = 99999;
        if(M == 0 && N == 0){
            break;
        }
        memset(map, '0', sizeof(map));
        memset(Distance, 0, sizeof(Distance));
        for(int i = 0 ; i < M ; i++){
            cin >> map[i];
            for(int j = 0 ; j < N ; j++){
                if(map[i][j] == 'o'){
                    nodeInfo.push_back(make_pair(make_pair(i,j),1));
                    v.push_back(1);
                }
            }
        }
        int nodeCount = 1;
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                if(map[i][j] == '*'){
                    nodeCount++;
                    nodeInfo.push_back(make_pair(make_pair(i,j), nodeCount));
                }
            }
        }
        getDistance();
        for(int i = 1 ; i < nodeInfo.size() ; i++){
            check[1] = true;
            v.push_back(nodeInfo[i].second);
            check[nodeInfo[i].second] = true;
            letsClean(i);
            v.pop_back();
            check[nodeInfo[i].second] = false;
        }
        if(ans >= 99999){
            cout << -1 << "\n";
        }
        else{
            cout << ans << "\n";
        }
        v.clear();
        nodeInfo.clear();
        dist.clear();
    }
}