#include <iostream>
#include <queue>

using namespace std;

int map[16][16];
int canGo;
bool visited[16][16];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void BFS(int startI, int startJ){
    canGo = 0;
    for(int i = 0 ; i < 16 ; i++){
        for(int j = 0 ; j < 16 ; j++){
            visited[i][j] = false;
        }
    }
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < 16 && nextJ >= 0 && nextJ < 16){
                if(!visited[nextI][nextJ] && (map[nextI][nextJ] == 0 || map[nextI][nextJ] == 3)){
                    q.push({nextI, nextJ});
                    visited[nextI][nextJ] = true;
                    if(map[nextI][nextJ] == 3){
                        canGo = 1;
                        return;
                    }
                }
            }
        }
    }
}

int main(){
    int T = 10;
    for(int t = 1 ; t <= T ; t++){
        char inputData[16][16];
        for(int i = 0 ; i < 16 ; i++){
            cin >> inputData[i];
            for(int j = 0 ; j < 16 ; j++){
                map[i][j] = int(inputData[i][j] - '0');
            }
        }
        for(int i = 0 ; i < 16 ; i++){
            for(int j = 0 ; j < 16 ; j++){
                if(map[i][j] == 2){
                    BFS(i,j);
                }
            }
        }
        cout << "#" << t << " " << canGo << "\n";
    }
    return 0;
}