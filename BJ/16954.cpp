// 16954

#include <iostream>
#include <vector>
#include <deque>

using namespace std;

char map[9][9];
bool visited[8][8];
int depth[8][8];

deque<pair<int, int>> wallInfo;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[9] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {-1,-1}, {-1,1}, {1,-1}, {1,1}, {0,0}};
void showdq(deque<pair<int, int>> dq){
    for(int i = 0 ; i < dq.size() ; i++){
        printf("(%d, %d) ", dq[i].first, dq[i].second);
    }
    cout << endl;
}
void show(){
    cout << endl;
    for(int i = 0 ; i < 8 ; i++){
        for(int j = 0 ; j < 8  ; j++){
            cout << map[i][j];
        }cout << endl;
    }cout << endl;
}
void moveWall(){
    int wallInfoSize = wallInfo.size();
    while(wallInfoSize--){
        int wallI = wallInfo.front().first;
        int wallJ = wallInfo.front().second;
        if(wallI == 7){
            wallInfo.pop_front();
            map[wallI][wallJ] = '.';
        }
        else{
            wallInfo.pop_front();
            map[wallI][wallJ] = '.';
            wallInfo.push_back(make_pair(wallI+1, wallJ));

        }
    }
    for(int i = 0 ; i < wallInfo.size() ; i++){
        map[wallInfo[i].first][wallInfo[i].second] = '#';
    }
}
void BFS(){
    deque<pair<int, int>> dq;
    dq.push_back(make_pair(7,0));
    map[7][0] = 'S';
    visited[7][0] = true;
    int rootDepth = 0;
    while(!dq.empty()){
        int currentI = dq.front().first;
        int currentJ = dq.front().second;
        dq.pop_front();
        if(depth[currentI][currentJ] == rootDepth + 1){
            rootDepth++;
            moveWall();
        }
        if(wallInfo.size() == 0 || currentI == 0){
            cout << 1 << endl;
            return;
        }
        if(map[currentI][currentJ] == 'S'){
            map[currentI][currentJ] = '.';
            for(int i  = 0 ; i < 9 ; i++){
                int nextI = currentI + moveDir[i].moveI;
                int nextJ = currentJ + moveDir[i].moveJ;
                if(nextI >= 0 && nextI < 8 && nextJ >= 0 && nextJ < 8){
                    if(map[nextI][nextJ] == '.'){
                        dq.push_back(make_pair(nextI, nextJ));
                        map[nextI][nextJ] = 'S';
                        visited[nextI][nextJ] = true;
                        depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                    }
                }
            }
        }
    }
    if(visited[0][7]){
        cout << 1 << endl;
    }
    else{
        cout << 0 << endl;
    }
}
int main(){
    for(int i = 0 ; i < 8 ; i++){
        cin >> map[i];
        for(int j = 0 ; j < 8 ; j++){
            if(map[i][j] == '#'){
                wallInfo.push_back(make_pair(i,j));
            }
        }
    }
    BFS();
    return 0;
}

/*
........
........
........
........
........
........
........
........
1

........
........
........
........
........
........
##......
........
0

........
........
........
........
........
.#......
#.......
.#......
0

........
........
........
........
........
.#######
#.......
........
1

........
........
........
........
#.......
.#######
#.......
........
0

..###.##
##...#.#
..#.#..#
#.#...#.
.#...#.#
.#.#..##
#..#..#.
..#....#
1

........
........
........
........
########
........
........
........
........
0
*/