#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int I, J;
int endI, endJ;
char map[51][51];
int visited[50][50];
typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,1}, {0,-1}};

void flood(){
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            if(map[i][j] == '*'){
                q.push({i,j});
                visited[i][j] = true;
            }
        }
    }
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
                if(!visited[nextI][nextJ] && (map[nextI][nextJ] == 'S' || map[nextI][nextJ] == '.')){
                    visited[nextI][nextJ] = true;
                    map[nextI][nextJ] = '*';
                }
            }
        }
    }
}

void escape(){
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            if(map[i][j] == 'S'){
                q.push({i,j});
                visited[i][j] = true;
            }
        }
    }
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == '.'){
                    visited[nextI][nextJ] = true;
                    map[nextI][nextJ] = 'S';
                }
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == 'D'){
                    visited[nextI][nextJ] = true;
                    map[nextI][nextJ] = 'S';
                }
            }
        }
    }
}

int main(){
    cin >> I >> J;
    for(int i = 0 ; i < I ; i++){
        cin >> map[i];
    }
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            if(map[i][j] == 'D'){
                endI = i;
                endJ = j;
            }
        }
    }
    for(int i = 0 ; i < 4 ; i++){
        int ansI = endI + moveDir[i].moveI;
        int ansJ = endJ + moveDir[i].moveJ;
        if(ansI >= 0 && ansI < I && ansJ >= 0 && ansJ < J){ 
            if(map[ansI][ansJ] == 'S'){
                cout << 1 << "\n";
                return 0;
            }
        }
    }
    int dayCount = 0;
    while(1){
        dayCount++;
        escape();
        flood();
        for(int i = 0 ; i < 4 ; i++){
            int ansI = endI + moveDir[i].moveI;
            int ansJ = endJ + moveDir[i].moveJ;
            if(ansI >= 0 && ansI < I && ansJ >= 0 && ansJ < J){
                if(map[ansI][ansJ] == 'S'){
                    cout << dayCount + 1 << "\n";
                    return 0;
                }
            }
        }
        if(dayCount > 2500){
            cout << "KAKTUS" << "\n";
            return 0;
        }
    }
}