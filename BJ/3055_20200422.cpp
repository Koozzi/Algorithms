#include <iostream>
#include <string>
#include <queue>
using namespace std;

string map[50];
int M, N, startI, startJ;

queue<pair<int,int>> water;
queue<pair<pair<int, int>, int>> q;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j];
        }cout << "\n";
    }
}

void flood(){
    int waterSize = water.size();
    for(int i = 0 ; i < waterSize ; i++){
        int currentI = water.front().first;
        int currentJ = water.front().second;
        water.pop();

        for(int j = 0 ; j < 4 ; j++){
            int nextI = currentI + moveDir[j].moveI;
            int nextJ = currentJ + moveDir[j].moveJ;

            if(nextI < 0 || nextJ < 0 || nextI >= M || nextJ >= N){
                continue;
            }

            if(map[nextI][nextJ] == '.' || map[nextI][nextJ] == 'S'){
                map[nextI][nextJ] = '*';
                water.push({nextI, nextJ});
            }
        }
    }
}

void BFS(){
    int depthCheck = 0;
    q.push({{startI, startJ}, 0});
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int depth = q.front().second;
        q.pop();

        if(depthCheck != depth){
            depthCheck++;
            flood();
        }

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextJ < 0 || nextI >= M || nextJ >= N){
                continue;
            }

            if(map[nextI][nextJ] == 'D' && map[currentI][currentJ] == 'S'){
                cout << depth+1 << "\n";
                exit(0);
            }

            if(map[nextI][nextJ] == '.'){
                q.push({{nextI, nextJ}, depth+1});
                map[nextI][nextJ] = 'S';
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 'S'){
                startI = i;
                startJ = j;
            }
            else if(map[i][j] == '*'){
                water.push({i,j});
            }
        }
    }
    BFS();
    cout << "KAKTUS" << "\n";
    return 0;
}