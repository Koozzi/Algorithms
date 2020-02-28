#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

vector<pair<int, int>> notWall;
vector<pair<int, int>> Wall;

int M, N, ans = 0;

int map[8][8];
int cmap[8][8];
bool visited[8][8];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << cmap[i][j]<< " ";
        }
        cout<< "\n";
    }
}

void mapCopy(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cmap[i][j] = map[i][j];
        }
    }
}

void BFS(){
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(cmap[i][j] == 2){
                q.push(make_pair(i,j));
                visited[i][j] = true;
            }
        }
    }
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(cmap[nextI][nextJ] == 0 && !visited[nextI][nextJ]){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    cmap[nextI][nextJ] = 2;
                }
            }
        }
    }
    int cnt = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(cmap[i][j] == 0){
                cnt++;
            }
        }
    }
    ans = max(ans, cnt);
}

void makeWall(int start){
    if(Wall.size() == 3){
        mapCopy();
        for(int i = 0 ; i < 3 ; i++){
            cmap[Wall[i].first][Wall[i].second] = 1;
        }
        BFS();
        return;
    }
    for(int i = start + 1 ; i < notWall.size() ; i++){
        Wall.push_back(make_pair(notWall[i].first, notWall[i].second));
        makeWall(i);
        Wall.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
            if(map[i][j] == 0){
                notWall.push_back(make_pair(i,j));
            }
        }
    }
    for(int i = 0 ; i < notWall.size() ; i++){
        Wall.push_back(make_pair(notWall[i].first, notWall[i].second));
        makeWall(i);
        Wall.pop_back();
    }
    cout << ans << "\n";
    return 0;
}