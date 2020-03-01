#include <iostream>
#include <queue>
#include <memory.h>
#include <algorithm>

using namespace std;

int M, N, ans = 65;
int beginI, beginJ, endI, endJ;
char map[51][51];
char cmap[9][9];
bool visited[8][8];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    for(int i = 0 ; i < 8 ; i++){
        for(int j = 0 ; j < 8 ; j++){
            cout << cmap[i][j] << " ";
        }
        cout << "\n";
    }
}

void BFS(int startI, int startJ){
    int cnt = 0;
    memset(visited, false, sizeof(visited));
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
            if(nextI >= 0 && nextI <  8 && nextJ >= 0 && nextJ < 8){
                if(!visited[nextI][nextJ]){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    if(cmap[nextI][nextJ] == cmap[currentI][currentJ]){
                        if(cmap[nextI][nextJ] == 'W'){
                            cmap[nextI][nextJ] = 'B';
                            cnt++;
                        }
                        else{
                            cmap[nextI][nextJ] = 'W';
                            cnt++;
                        }
                    }
                }
            }
        }
    }
    ans = min(ans, cnt);
}

void copyMap(int startI, int startJ){
    for(int i = 0 ; i < 8 ; i++){
        for(int j = 0 ; j < 8 ; j++){
            cmap[i][j] = map[i+startI][j+startJ];
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }
    for(int i = 0 ; i < M-7 ; i++){
        for(int j = 0 ; j < N-7 ; j++){
            copyMap(i,j);
            BFS(0,0);
            copyMap(i,j);
            BFS(0,7);
            copyMap(i,j);
            BFS(7,0);
            copyMap(i,j);
            BFS(7,7);
        }
    }
    cout << ans << "\n";
    return 0;
}

