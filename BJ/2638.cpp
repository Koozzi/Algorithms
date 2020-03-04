#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int M, N, startI, startJ;
int map[100][100];
bool visited[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j] << " ";
        }cout << "\n";
    }
}

int cheezeSize(){
    int size = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 1){
                size++;
            }
        }
    }
    return size;
}

void BFS(){
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    visited[0][0] = true;
    map[0][0] = 8;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && (map[nextI][nextJ] == 0 || map[nextI][nextJ] == 8)){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    map[nextI][nextJ] = 8;
                }
            }
        }
    }
}

void meltCheeze(){
    vector<pair<int, int>> v;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            int cnt = 0;
            for(int k = 0 ; k  < 4 ; k++){
                int nextI = i + moveDir[k].moveI;
                int nextJ = j + moveDir[k].moveJ;
                if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                    if(map[nextI][nextJ] == 8){
                        cnt++;
                    }
                }
            }
            if(cnt >= 2){
                v.push_back(make_pair(i,j));
            }
        }
    }
    for(int i = 0 ; i < v.size() ; i++){
        map[v[i].first][v[i].second] = 8;
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    int sec = 0;
    while(1){
        BFS();
        meltCheeze();
        sec++;
        if(cheezeSize() == 0){
            cout << sec << "\n";
            return 0;
        }
    }
}