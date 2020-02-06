#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

#define MAX_SIZE 50
using namespace std;

int w, h;
int island_count = 0;
int map[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE];

typedef struct{
    int y,x;
}Dir;
Dir moveDir[8] = {{-1,-1}, {0,-1}, {1,-1},{-1,0},{1,0},{-1,1},{0,1},{1,1}};

void BFS(int y, int x){
    queue<pair<int,int>> q;
    q.push({y,x});
    visited[y][x] = true;
    while(!q.empty()){
        int Y = q.front().first;
        int X = q.front().second;
        q.pop();
        for(int i = 0 ; i < 8 ; i++){
            int nextY = Y + moveDir[i].y;
            int nextX = X + moveDir[i].x;
            if(nextY >= 0 && nextY < h
            && nextX >= 0 && nextX < w
            && !visited[nextY][nextX]
            && map[nextY][nextX] == 1){
                visited[nextY][nextX] = true;
                q.push({nextY, nextX});
            }
        }
    }
}
int main(){
    while(1){
        cin >> w >> h;
        int cnt = 0;
        if(w == 0 && h == 0){
            break;
        }
        for(int i = 0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                cin >> map[i][j];
            }
        }
        for(int i = 0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                if(map[i][j] == 1 && !visited[i][j]){
                    BFS(i,j);
                    cnt++;
                }
            }
        }
        for(int i =0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                visited[i][j] = false;
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}