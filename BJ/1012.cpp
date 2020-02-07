#include <iostream>
#include <queue>

using namespace std;

int N, M, K;
int map[50][50] = {0};
bool visited[50][50];

typedef struct{
    int move_i, move_j;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void BFS(int start_i, int start_j){
    queue<pair<int, int>> q;
    q.push({start_i, start_j});
    visited[start_i][start_j] = true;
    while(!q.empty()){
        int current_i = q.front().first;
        int current_j = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int next_i = current_i + moveDir[i].move_i;
            int next_j = current_j + moveDir[i].move_j;
            if(next_i >= 0 && next_i < N && next_j >= 0 && next_j < M){
                if(!visited[next_i][next_j] && map[next_i][next_j] == 1){
                    q.push({next_i, next_j});
                    visited[next_i][next_j] = true;
                }
            }
        }
    }
}

int main(){
    int T, a, b;
    cin >> T;
    for(int t = 0 ; t < T ; t++){
        for(int i = 0 ; i < 50 ; i++){
            for(int j = 0 ; j < 50 ; j++){
                visited[i][j] = false;
                map[i][j] = 0;
            }
        }
        int ans = 0;
        cin >> M >> N >> K;
        for(int i = 0 ; i < K ; i++){
            cin >> a >> b;
            map[a][b] = 1;
        }
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
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