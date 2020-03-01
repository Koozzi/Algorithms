#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

int M, N, ans;
int map[1000][1000];
int depth[1000][1000];
bool visited[1000][1000];

vector<pair<int, int>> wall;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }
}

int BFS(){
    queue<pair<int, int>> q;
    q.push(make_pair(0,0));
    visited[0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == 0){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                }
            }
        }
    }
    if(visited[M-1][N-1]){
        return depth[M-1][N-1] + 1;
    }
    else{
        return 9999;
    }
}

int main(){
    cin >> M >> N;
    char inputData[1000][1000];
    for(int i = 0 ; i < M ; i++){
        cin >> inputData[i];
        for(int j = 0 ; j < N ; j++){
            map[i][j] = int(inputData[i][j] - '0');
            if(map[i][j] == 1){
                wall.push_back(make_pair(i,j));
            }
        }
    }

    ans = BFS();
    for(int i = 0 ; i < wall.size() ; i++){    
        memset(visited, false, sizeof(visited));
        memset(depth, 0, sizeof(depth));
        map[wall[i].first][wall[i].second] = 0;
        ans = min(ans, BFS());
        map[wall[i].first][wall[i].second] = 1;
    }
    if(ans == 9999){
        cout << -1 << "\n";
    }else{
        cout << ans << "\n";
    }
    
    return 0;
}