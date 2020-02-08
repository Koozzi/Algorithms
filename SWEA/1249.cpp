#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int M;
int map[102][102];
int cost[102][102];
bool visited[102][102];

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
        char inputData[102][102];
        for(int i = 0 ; i < M ; i++){
            cin >> inputData[i];
            for(int j = 0 ; j < M ; j++){
                map[i][j] = int(inputData[i][j] - '0');
            }
        }
        BFS();
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                cout << cost[i][j] << " ";
            }
            cout << "\n";
        }
        cout << "#" << t << " " << cost[M][M] << "\n";
    }
    return 0;
}