#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX_SIZE 101
using namespace std;
int N,M;
char input_data[MAX_SIZE][MAX_SIZE];
int map[MAX_SIZE][MAX_SIZE];
int depth[MAX_SIZE][MAX_SIZE] = {0};
bool visited[MAX_SIZE][MAX_SIZE];
vector<int> v_map[MAX_SIZE];

typedef struct{
    int y, x;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void bfs(){
    int y = 0, x = 0;
    depth[0][0] = 0;
    queue<pair<int, int>> q;
    visited[y][x] = true;
    q.push({y,x});
    while(!q.empty()){
        int Y = q.front().first;
        int X = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextY = Y + moveDir[i].y;
            int nextX = X + moveDir[i].x;
            if(nextY >= 0 && nextY < N
            && nextX >= 0 && nextX < M
            && !visited[nextY][nextX]
            && map[nextY][nextX] == 1){
                visited[nextY][nextX] = true;
                depth[nextY][nextX] = depth[Y][X] + 1;
                q.push({nextY,nextX});
            }
        }
    }
    return;
}

int main(){
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> input_data[i];
        for(int j = 0 ; j < M ; j++){
            map[i][j] = int(input_data[i][j]) - 48;
            visited[i][j] = false;
        }
    }
    bfs();
    if(visited[N-1][M-1]){
        cout << depth[N-1][M-1] + 1 << "\n";
    }
    else{
        cout << 0 << "\n";
    }
    
    return 0;
}

// 계속 "틀렸습니다" 라고 나온 이유
// MAX_SIZE 를 100 으로 설정했는데 
// 문자열을 받을 때는 마지막에 항상 NULL 값이 따라옴.
// MAX_SIZE 를 100 으로 설정을 하면 결국 나는 최대값을 99까지 밖에 못받는다는 소리임
// MAX_SIZE 를 101 로 바꿔주니까 바로 맞았습니다!! ^-^