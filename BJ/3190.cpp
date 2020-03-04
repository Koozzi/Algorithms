#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int M, appleNum, dirNum, snakeDir;
int currentI, currentJ, nextI, nextJ;
int second = 0;
int map[101][101];

deque<int> changeSecond;
deque<char> changeDir;

void show(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cout << map[i][j];
        }cout << "\n";
    }cout << "\n";
}

void Next(int d){
    if(d == 1){
        nextI = currentI - 1;
        nextJ = currentJ;
    }
    else if(d == 2){
        nextI = currentI;
        nextJ = currentJ + 1;
    }
    else if(d == 3){
        nextI = currentI + 1;
        nextJ = currentJ;
    }
    else{
        nextI = currentI;
        nextJ = currentJ - 1;
    } 
}

void moveSnake(){
    deque<pair<int ,int>> dq;
    dq.push_back(make_pair(1, 1));
    map[1][1] = 1;
    while(1){
        currentI = dq.back().first;
        currentJ = dq.back().second;
        Next(snakeDir);
        if(map[nextI][nextJ] == 1 || nextI == 0 || nextI == M+1 || nextJ == 0 || nextJ == M+1){
            second++;
            return;
        }
        else{
            if(map[nextI][nextJ] == 7){
                map[nextI][nextJ] = 1;
                dq.push_back(make_pair(nextI, nextJ));
            }
            else{
                map[nextI][nextJ] = 1;
                dq.push_back(make_pair(nextI, nextJ));
                int deleteI = dq.front().first;
                int deleteJ = dq.front().second;
                map[deleteI][deleteJ] = 0;
                dq.pop_front();
            }
            second++;
        }
        // cout << second << "\n";
        // show();
        if(changeSecond.size() != 0){
            if(second == changeSecond.front()){
                if(changeDir.front() == 'D'){
                    if(snakeDir == 1){
                        snakeDir = 2;
                    }
                    else if(snakeDir == 2){
                        snakeDir = 3;
                    }
                    else if(snakeDir == 3){
                        snakeDir = 4;
                    }
                    else{
                        snakeDir = 1;
                    }
                }
                else{
                    if(snakeDir == 1){
                        snakeDir = 4;
                    }
                    else if(snakeDir == 2){
                        snakeDir = 1;
                    }
                    else if(snakeDir == 3){
                        snakeDir = 2;
                    }
                    else{
                        snakeDir = 3;
                    }                
                }
                changeDir.pop_front();
                changeSecond.pop_front();
            }
        }
    }
}

int main(){
    snakeDir = 2;
    cin >> M >> appleNum;
    for(int i = 0 ; i < appleNum ; i++){
        int a, b;
        cin >> a >> b;
        map[a][b] = 7;
    }
    cin >> dirNum;
    for(int i = 0 ; i < dirNum ; i++){
        int a;
        char b;
        cin >> a >> b;
        changeSecond.push_back(a);
        changeDir.push_back(b);
    }
    moveSnake();
    cout << second << "\n";
    return 0;
}