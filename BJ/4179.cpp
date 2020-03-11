#include <iostream>
#include <deque>

using namespace std;

int M, N, I, J;
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
void spreadFire(){
    int fireSize = fireInfo.size();
    for(int i = 0 ; i < fireSize ; i++){
        int currentI = fireInfo[0].first;
        int currentJ = fireInfo[0].second;
        fireInfo.pop_front();
        for(int j = 0 ; j < 4 ; j++){
            int nextI = currentI + moveDir[j].moveI;
            int nextJ = currentJ + moveDir[j].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(map[nextI][nextJ] == 'J' || map[nextI][nextJ] == '.'){
                    fireInfo.push_back(make_pair(nextI, nextJ));
                    map[nextI][nextJ] = 'F';
                }
            }
        }
    }
}
void escape(){
    deque<pair<pair<int, int>, int>> dq;
    dq.push_back(make_pair(make_pair(I, J), 0));
    visited[I][J] = true;
    int depthCheck = 0;
    while(!dq.empty()){
        int currentI = dq.front().first.first;
        int currentJ = dq.front().first.second;
        int currentD = dq.front().second;
        if(currentD != depthCheck){ 
            // 자식 노드를 방문하면 불 확산
            depthCheck++;
            spreadFire();
        }
        if(map[currentI][currentJ] == 'F'){ 
            // 불을 확산했는데 현재 노드의 위치에 불이 있으면 스킵
            dq.pop_front();
            continue;
        }
        if(currentI == 0 || currentI == M-1 || currentJ == 0 || currentJ == N-1){
            // 불을 확산시켰음에도 불구하고 현재 노드가 가장자리에 도착을 했으면 깊이 + 1 을 출력
            cout << currentD + 1 << endl;
            return;
        }
        dq.pop_front();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == '.'){
                    dq.push_back(make_pair(make_pair(nextI, nextJ), currentD + 1));
                    visited[nextI][nextJ] = true;
                    map[nextI][nextJ] = 'J';
                }
            }
        }
    }
    cout << "IMPOSSIBLE" << endl;
}
int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 'F'){
                fireInfo.push_back(make_pair(i, j));
            }
            else if(map[i][j] == 'J'){
                I = i;
                J = j;
            }
        }
    }
    escape();
    return 0;
}


/*
4 4
####
#JF#
#..#
#..#
-> 3

5 5
##.##
#...#
#FJ.#
#...#
#####
-> 3

5 5
....F
...J#
....#
....#
...#.
-> 4

3 3
F.F
.J.
F.F
-> IMPOSSIBLE

1 1 
J
-> 1
*/
