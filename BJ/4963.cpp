#include <iostream>
#include <queue>

using namespace std;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[8] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {-1,-1}, {-1,1}, {1,1}, {1,-1}};

int M, N;
int map[50][50];
bool visited[50][50];

void init(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            map[i][j] = 0;
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
                q.push({nextI,nextJ});
                visited[nextI][nextJ] = true;
            }
        }
    }
}

int main(){
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

// #include <algorithm>
// #include <iostream>
// #include <vector>
// #include <queue>

// #define MAX_SIZE 50
// using namespace std;

// int w, h;
// int island_count = 0;
// int map[MAX_SIZE][MAX_SIZE];
// bool visited[MAX_SIZE][MAX_SIZE];

// typedef struct{
//     int y,x;
// }Dir;
// Dir moveDir[8] = {{-1,-1}, {0,-1}, {1,-1},{-1,0},{1,0},{-1,1},{0,1},{1,1}};

// void BFS(int y, int x){
//     queue<pair<int,int>> q;
//     q.push({y,x});
//     visited[y][x] = true;
//     while(!q.empty()){
//         int Y = q.front().first;
//         int X = q.front().second;
//         q.pop();
//         for(int i = 0 ; i < 8 ; i++){
//             int nextY = Y + moveDir[i].y;
//             int nextX = X + moveDir[i].x;
//             if(nextY >= 0 && nextY < h
//             && nextX >= 0 && nextX < w
//             && !visited[nextY][nextX]
//             && map[nextY][nextX] == 1){
//                 visited[nextY][nextX] = true;
//                 q.push({nextY, nextX});
//             }
//         }
//     }
// }
// int main(){
//     while(1){
//         cin >> w >> h;
//         int cnt = 0;
//         if(w == 0 && h == 0){
//             break;
//         }
//         for(int i = 0 ; i < h ; i++){
//             for(int j = 0 ; j < w ; j++){
//                 cin >> map[i][j];
//             }
//         }
//         for(int i = 0 ; i < h ; i++){
//             for(int j = 0 ; j < w ; j++){
//                 if(map[i][j] == 1 && !visited[i][j]){
//                     BFS(i,j);
//                     cnt++;
//                 }
//             }
//         }
//         for(int i =0 ; i < h ; i++){
//             for(int j = 0 ; j < w ; j++){
//                 visited[i][j] = false;
//             }
//         }
//         cout << cnt << "\n";
//     }
//     return 0;
// }