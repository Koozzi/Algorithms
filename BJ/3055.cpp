#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int M, N, destI, destJ;
bool visited[50][50];

string map[50];

queue<pair<int, int>> water;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j];
        }cout << "\n";
    }
}
void flood(){
    int currentSize = water.size();
    for(int i = 0 ; i < currentSize ; i++){
        int currentI = water.front().first;
        int currentJ = water.front().second;
        water.pop();

        for(int j = 0 ; j < 4 ; j++){
            int nextI = currentI + moveDir[j].moveI;
            int nextJ = currentJ + moveDir[j].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(map[nextI][nextJ] != 'D' && map[nextI][nextJ] != 'X' && map[nextI][nextJ] != '*'){
                map[nextI][nextJ] = '*';
                water.push({nextI, nextJ});
            }
        }
    }
}
void BFS(int startI, int startJ){
    int depthCheck = 0;
    queue<pair<pair<int, int>, int>> q;
    q.push({{startI, startJ}, 0});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int depth = q.front().second;
        q.pop();

        if(currentI == destI && currentJ == destJ){
            cout << depth << "\n";
            exit(0);
        }

        if(depth != depthCheck){
            depthCheck++;
            flood();
        }

        if(map[currentI][currentJ] != 'S') continue;

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] != '*' && map[nextI][nextJ] != 'X'){
                map[nextI][nextJ] = 'S';
                q.push({{nextI, nextJ}, depth+1});
            }
        }
    }
}

int main(){
    int startI, startJ;
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == '*'){
                water.push({i,j});
            }
            if(map[i][j] == 'S'){
                startI = i;
                startJ = j;
            }
            if(map[i][j] =='D'){
                destI = i;
                destJ = j;
            }
        }
    }

    BFS(startI, startJ);

    cout << "KAKTUS" << "\n";

    return 0;
}
// #include <iostream>
// #include <queue>
// #include <memory.h>

// using namespace std;

// int I, J;
// int endI, endJ;
// char map[51][51];
// int visited[50][50];
// typedef struct{
//     int moveI, moveJ;
// }Dir;
// Dir moveDir[4] = {{-1,0}, {1,0}, {0,1}, {0,-1}};

// void flood(){
//     memset(visited, false, sizeof(visited));
//     queue<pair<int, int>> q;
//     for(int i = 0 ; i < I ; i++){
//         for(int j = 0 ; j < J ; j++){
//             if(map[i][j] == '*'){
//                 q.push({i,j});
//                 visited[i][j] = true;
//             }
//         }
//     }
//     while(!q.empty()){
//         int currentI = q.front().first;
//         int currentJ = q.front().second;
//         q.pop();
//         for(int i = 0 ; i < 4 ; i++){
//             int nextI = currentI + moveDir[i].moveI;
//             int nextJ = currentJ + moveDir[i].moveJ;
//             if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
//                 if(!visited[nextI][nextJ] && (map[nextI][nextJ] == 'S' || map[nextI][nextJ] == '.')){
//                     visited[nextI][nextJ] = true;
//                     map[nextI][nextJ] = '*';
//                 }
//             }
//         }
//     }
// }

// void escape(){
//     memset(visited, false, sizeof(visited));
//     queue<pair<int, int>> q;
//     for(int i = 0 ; i < I ; i++){
//         for(int j = 0 ; j < J ; j++){
//             if(map[i][j] == 'S'){
//                 q.push({i,j});
//                 visited[i][j] = true;
//             }
//         }
//     }
//     while(!q.empty()){
//         int currentI = q.front().first;
//         int currentJ = q.front().second;
//         q.pop();
//         for(int i = 0 ; i < 4 ; i++){
//             int nextI = currentI + moveDir[i].moveI;
//             int nextJ = currentJ + moveDir[i].moveJ;
//             if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
//                 if(!visited[nextI][nextJ] && map[nextI][nextJ] == '.'){
//                     visited[nextI][nextJ] = true;
//                     map[nextI][nextJ] = 'S';
//                 }
//                 if(!visited[nextI][nextJ] && map[nextI][nextJ] == 'D'){
//                     visited[nextI][nextJ] = true;
//                     map[nextI][nextJ] = 'S';
//                 }
//             }
//         }
//     }
// }

// int main(){
//     cin >> I >> J;
//     for(int i = 0 ; i < I ; i++){
//         cin >> map[i];
//     }
//     for(int i = 0 ; i < I ; i++){
//         for(int j = 0 ; j < J ; j++){
//             if(map[i][j] == 'D'){
//                 endI = i;
//                 endJ = j;
//             }
//         }
//     }
//     for(int i = 0 ; i < 4 ; i++){
//         int ansI = endI + moveDir[i].moveI;
//         int ansJ = endJ + moveDir[i].moveJ;
//         if(ansI >= 0 && ansI < I && ansJ >= 0 && ansJ < J){ 
//             if(map[ansI][ansJ] == 'S'){
//                 cout << 1 << "\n";
//                 return 0;
//             }
//         }
//     }
//     int dayCount = 0;
//     while(1){
//         dayCount++;
//         escape();
//         flood();
//         for(int i = 0 ; i < 4 ; i++){
//             int ansI = endI + moveDir[i].moveI;
//             int ansJ = endJ + moveDir[i].moveJ;
//             if(ansI >= 0 && ansI < I && ansJ >= 0 && ansJ < J){
//                 if(map[ansI][ansJ] == 'S'){
//                     printf("구치훈 바보 멍청이 똥개 넌 메롱이야!");
//                     cout << dayCount + 1 << "\n";
//                     return 0;
//                 }
//             }
//         }
//         if(dayCount > 2500){
//             cout << "KAKTUS" << "\n";
//             return 0;
//         }
//     }
// }