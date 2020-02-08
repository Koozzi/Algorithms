#include <iostream>
#include <queue>

using namespace std;

int M,N;
int ans = 0;
int map[8][8] = {0};
int copyMap[8][8] = {0};
bool visited[8][8];

typedef struct{
    int move_i, move_j;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void BFS(){
    queue<pair<int ,int>> q;
    
    int temp[8][8] = {0};

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            temp[i][j] = copyMap[i][j];
        }
    }
    
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(temp[i][j] == 2){
                q.push({i,j});
                visited[i][j] = true;
            }
        }
    }
    while(!q.empty()){
        int current_i = q.front().first;
        int current_j = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int next_i = current_i + moveDir[i].move_i;
            int next_j = current_j + moveDir[i].move_j;
            if(next_i >= 0 && next_i < M && next_j >= 0 && next_j < N){
                if(!visited[next_i][next_j] && temp[next_i][next_j] == 0){
                    temp[next_i][next_j] = 2;
                    q.push({next_i, next_j});
                    visited[next_i][next_j] = true;
                }
            }
        }
    }
    for(int i = 0 ; i < 8 ; i++){ // 방문 배열 초기화
        for(int j = 0 ; j < 8 ; j++){
            visited[i][j] = false;
        }
    }
    int countZero = 0; // 안전지역 수 세기
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(temp[i][j] == 0){
                countZero++;
            }
        }
    }
    if(countZero >= ans){
        ans = countZero;
    }
}

void makeWall(int cnt){
    if(cnt == 3){
        BFS();
        return;
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(copyMap[i][j] == 0){
                copyMap[i][j] = 1;
                makeWall(cnt + 1);
                copyMap[i][j] = 0;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j <  N ; j++){
            cin >> map[i][j];
        }
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0){
                for(int k = 0 ; k < M ; k++){
                    for(int l = 0 ; l < N ; l++){
                        copyMap[k][l] = map[k][l];
                    }
                }
                copyMap[i][j] = 1;
                makeWall(1);
                copyMap[i][j] = 0;
            }
        }
    }


    cout << ans << "\n";
    return 0;
}