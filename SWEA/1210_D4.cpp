#include <iostream>
#include <queue>

using namespace std;

int ans = 0;
int map[100][100] = {0};
bool visited[100][100]; 

typedef struct{
    int move_i, move_j;
}Dir;

Dir moveDir[3] = {{0, 1}, {0, -1}, {-1, 0}};


void BFS(int start_i, int start_j){
    for(int i = 0 ; i < 100 ; i++){
        for(int j = 0 ; j < 100 ; j++){
            visited[i][j] = false;
        }
    }
    queue<pair<int, int>> q;
    q.push({start_i, start_j});
    visited[start_i][start_j] = true;
    while(!q.empty()){
        int current_i = q.front().first;
        int current_j = q.front().second;
        q.pop();
        for(int i = 0 ; i < 3 ; i++){
            int next_i = current_i + moveDir[i].move_i;
            int next_j = current_j + moveDir[i].move_j;
            if(next_i >= 0 && next_j >= 0 && next_j < 100){
                if(map[next_i][next_j] == 1 && !visited[next_i][next_j]){
                    q.push({next_i, next_j});
                    visited[next_i][next_j] = true;
                    if(next_i == 0){
                        ans = next_j;
                    }
                    break;
                }

            }
        }
    }
}

int main(){
    int T = 10;
    for(int t = 1 ; t <= T ; t++){
        int test_num;
        cin >> test_num;
        int start_i, start_j;
        for(int i = 0 ; i < 100 ; i++){
            for(int j = 0 ; j < 100 ; j++){
                cin >> map[i][j];
                if(map[i][j] == 2){
                    start_i = i;
                    start_j = j;
                }
            }
        }
        BFS(start_i, start_j);
        cout << "#" << t << " " << ans << "\n";
    }
    return 0;
}