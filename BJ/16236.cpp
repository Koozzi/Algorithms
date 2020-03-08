#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <memory.h>


using namespace std;

int M, ans = 0;
int Tlqkf = 0;
int sharkI, sharkJ, sharkSize = 2;
int eatSize = 0;
int shortest;
int map[20][20];
int depth[20][20];

bool visited[20][20];
int check[20][20];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cout << map[i][j] << " ";
        }cout << "\n";
    }
}

void init(){
    memset(visited, false, sizeof(visited));
    memset(check, 0, sizeof(check));
    memset(depth, 0, sizeof(depth));
    shortest = 99999;
}
bool isThereAnyFish(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            if(map[i][j] < sharkSize && map[i][j] != 0 && map[i][j] != 9){
                return true;
            }
        }
    }
    return false;
}
void BFS(){
    init();
    Tlqkf = 0;
    queue<pair<int, int>> q;
    q.push(make_pair(sharkI, sharkJ));
    visited[sharkI][sharkJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] <= sharkSize){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                    if(map[nextI][nextJ] >= 1 && map[nextI][nextJ] <= 6 && map[nextI][nextJ] < sharkSize){
                        check[nextI][nextJ] = depth[nextI][nextJ];
                        shortest = min(shortest, check[nextI][nextJ]);
                        Tlqkf++;
                    }
                }
            }
        }
    }
    bool forBreak = false;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            if(check[i][j] == shortest){
                ans += check[i][j];
                eatSize++;
                if(sharkSize == eatSize){
                    eatSize = 0;
                    sharkSize++;
                }
                map[sharkI][sharkJ] = 0; // 현재 상어 자리를 0으로
                sharkI = i; // 상어 위치 바꿔줌
                sharkJ = j; // 상어 위치 바꿔줌
                map[sharkI][sharkJ] = 9; //
                forBreak = true;
                break;
            }
        }
        if(forBreak){
            break;
        }
    }
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
            if(map[i][j] == 9){
                sharkI = i;
                sharkJ = j;
            }
        }
    }
    while(isThereAnyFish()){
        BFS();
        if(Tlqkf == 0){
            cout << ans << endl;
            return 0;
        }
    }
    cout << ans << endl;
    return 0;
}