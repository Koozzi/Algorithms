#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int N, M;
int map[1000][1000];
int depth[1000][1000];
bool visit[1000][1000];
queue<pair<int, int>> tomato;

typedef struct{
    int moveI, moveJ;
} Dir;
Dir moveDir[4] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void BFS(){
    queue<pair<int, int>> q;
    while(!tomato.empty()){
        int I = tomato.front().first;
        int J = tomato.front().second;
        tomato.pop();
        q.push({I, J});
        depth[I][J] = 0;
    }
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= M) continue;

            if(map[nextI][nextJ] == 0){
                q.push({nextI, nextJ});
                map[nextI][nextJ] = 1;
                depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
            }
        }
    }
    int ans = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            if(map[i][j] == 1){
                ans = max(ans, depth[i][j]);
            }
            else if(map[i][j] == 0){
                cout << -1 << "\n";
                return;
            }
        }
    }
    cout << ans << "\n";
    return;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
            if(map[i][j] == 1){
                tomato.push({i, j});
            }
        }
    }
    BFS();
}