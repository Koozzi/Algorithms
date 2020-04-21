#include <iostream>
#include <queue>
using namespace std;

int M, N;
int map[50][50];
bool visited[50][50];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[8] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {-1,-1}, {-1,1}, {1,1}, {1,-1}};

void init(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            visited[i][j] = false;
        }
    }
}

void BFS(int startI, int startJ){
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 8 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] == 1){
                q.push({nextI, nextJ});
                visited[nextI][nextJ] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    while(1){
        int ans = 0;
        cin >> N >> M;
        if(M == 0 && N == 0) break;
        init();
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                cin >> map[i][j];
            }
        }

        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                if(!visited[i][j] && map[i][j] == 1){
                    BFS(i, j);
                    ans++;
                }
            }
        }

        cout << ans << "\n";
    }
    return 0;
}