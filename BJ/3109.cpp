#include <iostream>
#include <string>
using namespace std;

int M, N;

string map[10000];
bool visited[10000][500];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[3] = {{-1,1}, {0,1}, {1,1}};

void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j];
        }cout << endl;
    }
}

bool pipe(int startI, int startJ){
    visited[startI][startJ] = true;
    if(startJ == N-1){
        return true;
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            int nextI = startI + moveDir[i].moveI;
            int nextJ = startJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(map[nextI][nextJ] == '.' && !visited[nextI][nextJ]){
                    if(pipe(nextI, nextJ)){
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }
    int cnt = 0;
    for(int i = 0 ; i < M ; i++){
        cnt += pipe(i,0);
    }
    cout << cnt << endl;
    return 0; 
}

/*
5 5
.xx..
..x..
.....
...x.
...x.
-> 2

5 6
..xx..
...x..
...x..
...x..
..x...
-> 1

7 7
.x...x.
.x.x..x
....x..
..x....
...x.x.
.x.x.x.
.....x.
-> 3

100 5
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
...x.
...x.
.....
...x.
...x.
...x.
.....
.....
..x..
..x..
.....
..x..
.....
..x..
.....
-> 92
*/