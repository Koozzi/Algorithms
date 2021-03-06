#include <iostream>
#include <queue>

using namespace std;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int M, N, map[1000][1000];
bool visited[1000][1000];

void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j] << " ";
        }cout << "\n";
    }
}

void BFS(){
    queue<pair<pair<int, int>, int>> q;

    int maxDepth = 0;

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 1){
                q.push({{i, j}, 0});
                visited[i][j] = true;
            }
        }
    }

    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentD = q.front().second;
        q.pop();

        maxDepth = max(maxDepth, currentD);

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] == 0){
                q.push({{nextI, nextJ}, currentD + 1});
                visited[nextI][nextJ] = true;
                map[nextI][nextJ] = 1;
            }
        }
    }

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0){
                cout << -1 << "\n";
                return;
            }
        }
    }

    cout << maxDepth << "\n";
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    BFS();
    return 0;
}

// #include <iostream>
// #include <queue>

// using namespace std;

// int M, N, dayCount = 0, zeroCount = 0;
// int map[1001][1001] = {0};
// int depth[1001][1001] = {0};
// bool visited[1001][1001] = {0};

// typedef struct{
//     int move_i, move_j;
// }Dir;

// Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

// void BFS(){
//     queue<pair<int, int>> q;
//     for(int i = 1 ; i <= N ; i++){
//         for(int j = 1 ; j <= M ; j++){
//             printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
//             if(map[i][j] == 1){
//                 q.push({i,j});
//                 visited[i][j] = true;
//             }
//         }
//     }
//     while(!q.empty()){
//         int current_i = q.front().first;
//         int current_j = q.front().second;
//         q.pop();
//         for(int i = 0 ; i < 4 ; i++){
//             int next_i = current_i + moveDir[i].move_i;
//             int next_j = current_j + moveDir[i].move_j;
//             if(next_i >= 1 && next_i <= N && next_j >= 1 && next_j <= M){
//                 if(!visited[next_i][next_j] && map[next_i][next_j] == 0){
//                     q.push({next_i, next_j});
//                     visited[next_i][next_j] = true;
//                     depth[next_i][next_j] = depth[current_i][current_j] + 1;
//                     map[next_i][next_j] = 1;
//                 }
//             }
//         }
//     }
// }   

// int main(){
//     cin >> M >> N;
//     for(int i = 1 ; i <= N ; i++){
//         for(int j = 1 ; j <= M ; j++){
//             cin >> map[i][j];
//         }
//     }

//     BFS();
    
//     for(int i = 1 ; i <= N ; i++){
//         for(int j = 1 ; j <= M ; j++){
//             if(depth[i][j] >= dayCount){
//                 dayCount = depth[i][j];
//             }
//             if(map[i][j] == 0){
//                 zeroCount++;
//             }
//         }
//     }
//     if(zeroCount == 0){
//         cout << dayCount << "\n";
//         printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
//     }
//     else{
//         cout << -1 << "\n";
//     }    
    
//     return 0;
// }

/*
BFS 동시진행 ( root node 가 2개 이상일 경우)
본인은 원래 BFS를 구현할 때 항상 root node 가 하나였음
이 문제에서는 root node 가 2개 이상이 될 수 있었음
처음에는 동시 진행을 어떻게 해? 라고 생각을 했지만 
그 시작점들이 root node 가 아닌 root node 의 자식들이라 생각하면 된다. 
Line 19 ~ 26 참조
*/