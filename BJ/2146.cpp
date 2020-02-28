#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <stdio.h>

using namespace std;

int N, section = 1;
int map[100][100];
bool notBound[100][100];
bool visited[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void show(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }
}

void BFS(int startI, int startJ){
    queue<pair<int, int>> q;
    q.push(make_pair(startI, startJ));
    visited[startI][startJ] = true;
    map[startI][startJ] = section;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < N && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] != 0){
                    map[nextI][nextJ] = section;
                    visited[nextI][nextJ] = true;
                    q.push(make_pair(nextI, nextJ));
                }
            }
        }
    }
}
void boundary(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            int check = 0;
            for(int k = 0 ; k < 4 ; k++){
                int nextI = i + moveDir[k].moveI;
                int nextJ = j + moveDir[k].moveJ;
                if(nextI >= 0 && nextI < N && nextJ >= 0 && nextJ < N){
                    if(map[nextI][nextJ] == 0){
                        check++;
                    }
                }
            }
            if(check == 0){
                notBound[i][j] = true;
            }
        }
    }
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(notBound[i][j]){
                map[i][j] = 0;
            }
        }
    }
}

int makeBridge(int sect, int startI, int startJ){
    int minLength = 201;
    int destI, destJ;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] != sect && map[i][j] != 0){
                minLength = min(minLength, abs(startI - i) + abs(startJ - j) - 1);
            }
        }
    }
    return minLength;
}

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] != 0 && !visited[i][j]){
                BFS(i,j);
                section++;
            }
        }
    }
    boundary();
    int ans = 201;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] != 0){
                ans = min(ans, makeBridge(map[i][j], i, j));
            }
        }
    }
    cout << ans << "\n";

    return 0;
}