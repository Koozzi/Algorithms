#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

int N, M, cnt;
int map[50][50];
bool visit[50][50];

typedef struct{
    int moveI, moveJ;
} Dir;
Dir moveDir[8] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,-1}, {-1,1}};

void initSet(){
    cnt = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            map[i][j] = 0;
            visit[i][j] = false;
        }
    }
}

void BFS(int startI, int startJ){
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visit[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 8 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= M) continue;

            if(map[nextI][nextJ] == 1 && !visit[nextI][nextJ]){
                q.push({nextI, nextJ});
                visit[nextI][nextJ] = true;
            } 
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while(1){
        cin >> M >> N;
        initSet();
        if(N == 0 && M == 0) break;
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                cin >> map[i][j];
            }
        }
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                if(!visit[i][j] && map[i][j] == 1){
                    BFS(i,j);
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}