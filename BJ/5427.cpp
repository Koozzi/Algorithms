#include <iostream>
#include <memory.h>
#include <deque>

using namespace std;

int M, N, startI, startJ;

char map[1001][1001];
bool visited[1000][1000];

deque<pair<int, int>> fireInfo;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j];
        }cout << endl;
    }
}
void init(){
    fireInfo.clear();
    memset(visited, false, sizeof(visited));
    memset(map, '\0', sizeof(map));
}
void spreadFire(){
    int fireSize = fireInfo.size();
    for(int i = 0 ; i < fireSize ; i++){
        int currentI = fireInfo.front().first;
        int currentJ = fireInfo.front().second;
        fireInfo.pop_front();
        for(int j = 0 ; j < 4 ; j++){
            int nextI = currentI + moveDir[j].moveI;
            int nextJ = currentJ + moveDir[j].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(map[nextI][nextJ] == '@' || map[nextI][nextJ] == '.'){
                    fireInfo.push_back(make_pair(nextI, nextJ));
                    map[nextI][nextJ] = '*';
                }
            }
        }
    }
}
void escape(){
    deque<pair<pair<int, int>, int>> dq;
    dq.push_back(make_pair(make_pair(startI, startJ), 0));
    visited[startI][startJ] = true;
    int depthCheck = 0;
    while(!dq.empty()){
        int currentI = dq.front().first.first;
        int currentJ = dq.front().first.second;
        int depth = dq.front().second;
        if(depthCheck != depth){
            depthCheck++;
            spreadFire();
        }
        if(map[currentI][currentJ] == '*'){
            dq.pop_front();
            continue;
        }
        if(currentI == 0 || currentJ == 0 || currentI == M-1 || currentJ == N-1){
            cout << depth + 1 << endl;
            return;
        }
        dq.pop_front();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == '.'){
                    dq.push_back(make_pair(make_pair(nextI, nextJ), depth + 1));
                    map[nextI][nextJ] = '@';
                }
            }
        }
    }
    cout << "IMPOSSIBLE" << endl;
}
int main(){
    int T;
    cin >> T;
    while(T--){
    init();
    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == '*'){
                fireInfo.push_back(make_pair(i,j));
            }
            else if(map[i][j] == '@'){
                startI = i;
                startJ = j;
            }
        }        
    }
    escape();
    }
    return 0;
}

/*
4 3
####
#*@.
####
-> 2

7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
-> 5

7 4
###.###
#....*#
#@....#
.######
-> IMPOSSIBLE

5 5
.....
.***.
.*@*.
.***.
.....
->IMPOSSIBLE

3 3
###
#@#
###
-> IMPOSSIBLE


1 1
@
-> 1

6 5
######
#....#
#..@.#
#....#
######
-> IMPOSSIBLE

*/