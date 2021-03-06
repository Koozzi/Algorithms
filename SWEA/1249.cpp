#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int M;
int map[100][100];
int cost[100][100];
bool visited[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void BFS(){
    queue<pair<int, int>> q;
    q.push({0,0});
    visited[0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
                if(!visited[nextI][nextJ] 
                || cost[nextI][nextJ] > cost[currentI][currentJ] + map[nextI][nextJ]){
                    cost[nextI][nextJ] = cost[currentI][currentJ] + map[nextI][nextJ];
                    visited[nextI][nextJ] = true;
                    q.push({nextI, nextJ});
                }
            }
        }
    }
}

void init(){
    memset(cost, 0, sizeof(cost));
    memset(visited, false, sizeof(visited));
}

int main(){
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        init();
        cin >> M;
        char inputData[101][101];
        for(int i = 0 ; i < M ; i++){
            cin >> inputData[i];
            for(int j = 0 ; j < M ; j++){
                map[i][j] = int(inputData[i][j] - '0');
            }
        }
        BFS();
        cout << "#" << t << " " << cost[M-1][M-1] << "\n";
    }
    return 0;
}