#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <deque>

using namespace std;

int M, N, locI, locJ, Dir;
int currentI, currentJ, currentDir, nextI, nextJ, nextDir;
int map[50][50];

void ready(int startI, int startJ, int startDir){
    if(startDir == 0){
        nextI = startI;
        nextJ = startJ - 1;
    }
    else if(startDir == 1){
        nextI = startI - 1;
        nextJ = startJ;
    }
    else if(startDir == 2){
        nextI = startI;
        nextJ = startJ + 1;
    }
    else{
        nextI = startI + 1;
        nextJ = startJ;
    }
}

void changeDir(int startDir){
    if(startDir == 0){
        nextDir = 3;
    }
    else if(startDir == 1){
        nextDir = 0;
    }
    else if(startDir == 2){
        nextDir = 1;
    }
    else{
        nextDir = 2;
    }
}

void letsClean(int startI, int startJ, int startDir){
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{startI, startJ},{startDir, 0}});
    map[startI][startJ] = 2;
    while(!q.empty()){
        currentI = q.front().first.first;
        currentJ = q.front().first.second;
        currentDir = q.front().second.first;
        q.pop();
        ready(currentI, currentJ, currentDir);
        if(map[nextI][nextJ] == 0){
            changeDir(currentDir);
            q.push({{nextI, nextJ},{nextDir, 0}});
            map[nextI][nextJ] = 2; 
        }
        else if(map[nextI][nextJ] == 2){
            changeDir(currentDir);
            q.push({{currentI, currentJ},{nextDir, 0}});
        }
        else if()
    }
}

int main(){
    cin >> M >> N >> locI >> locJ >> Dir;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    letsClean(locI, locJ, Dir);
}