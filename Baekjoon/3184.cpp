#include <iostream>
#include <vector>
#include <queue>
#define RMAX_SIZE 251
#define CMAX_SIZE 251

using namespace std;
char fence[RMAX_SIZE][CMAX_SIZE];
bool visited[RMAX_SIZE][CMAX_SIZE];
vector<int> connected[251];
int n, m;
int final_sheep = 0;
int final_wolf = 0;

typedef struct{
    int y,x;
}Dir;
Dir moveDir[4] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void bfs(int y, int x){
    int sheep = 0, wolf = 0;
    queue<pair<int, int>> q;
    q.push({y,x});
    visited[y][x] = true;
    if(fence[y][x] == 'o'){
        sheep++;
    }
    else if(fence[y][x] == 'v'){
        wolf++;
    }
    while(!q.empty()){
        int Y = q.front().first;
        int X = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextY = Y + moveDir[i].y;
            int nextX = X + moveDir[i].x;

            if(0 <= nextY && nextY < n
            && 0 <= nextX && nextX < m
            && !visited[nextY][nextX]
            && fence[nextY][nextX] != '#'){
                visited[nextY][nextX] = true;
                if(fence[nextY][nextX] == 'o'){
                    sheep++;
                }
                else if(fence[nextY][nextX] == 'v'){
                    wolf++;
                }
                q.push({nextY, nextX});
            }
        }
    }
    if(sheep > wolf){
        final_sheep += sheep;
    }
    else{
        final_wolf += wolf;
    }
}

int main(){
    
    cin >> n >> m;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            cin >> fence[i][j];
        }
    }
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if((fence[i][j] == 'v' || fence[i][j] == 'o') && !visited[i][j] ){
                bfs(i,j);
            }
        }
    }
    cout << final_sheep << " " << final_wolf << "\n";
    return 0;
}