#include <iostream>
#include <queue>

using namespace std;

int map_size, begin_i, begin_j, end_i, end_j, cnt = 0;
int map[300][300] = {0};
int depth[300][300] = {0};
bool visited[300][300];

typedef struct{
    int move_i, move_j;
}Dir;
Dir moveDir[8] = {{-2 , 1}, {-1, 2}, {1, 2}, {2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};

void BFS(int I, int J){
    queue<pair<int, int>> q;
    visited[I][J] = true;
    q.push({I,J});
    while(!q.empty()){
        int current_I = q.front().first;
        int current_J = q.front().second;
        q.pop();
        for(int i = 0 ; i < 8 ; i++){
            int next_I = current_I + moveDir[i].move_i;
            int next_J = current_J + moveDir[i].move_j;
            if(next_I >= 0 && next_J <= map_size
            && next_J >= 0 && next_J <= map_size){
                if(!visited[next_I][next_J]){
                    if(map[next_I][next_J] == 1){
                        depth[next_I][next_J] = depth[current_I][current_J] + 1;
                        return;
                    }
                    else{
                        q.push({next_I, next_J});
                        visited[next_I][next_J] = true;
                        depth[next_I][next_J] = depth[current_I][current_J] + 1;
                    }
                }
            }
        }
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 0 ; t < T ; t++){
        cin >> map_size;
        for(int i = 0 ; i < map_size ; i++){
            for(int j = 0 ; j < map_size ; j++){
                visited[i][j] = false;
                depth[i][j] = 0;
            }
        }
        cin >> begin_i >> begin_j >> end_i >> end_j;
        map[end_i][end_j] = 1;
        visited[begin_i][begin_j] = true;
        BFS(begin_i, begin_j);
        cout << depth[end_i][end_j] << "\n";
    }
    return 0;
}