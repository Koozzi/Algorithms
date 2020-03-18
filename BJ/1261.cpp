#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#define MAX_NUM 2147483647
using namespace std;

int M, N;
int map[100][100];
int dist[100][100];
char inputData[101][101];

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
void BFS(){
    queue<pair<int, int>> q;
    q.push(make_pair(0,0));
    dist[0][0] = 0;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(dist[currentI][currentJ] + map[nextI][nextJ] < dist[nextI][nextJ]){
                    dist[nextI][nextJ] = dist[currentI][currentJ] + map[nextI][nextJ];
                    q.push(make_pair(nextI, nextJ));
                }
            }
        }
    }
}
int main(){
    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> inputData[i];
        for(int j = 0 ; j < N ; j++){
            map[i][j] = inputData[i][j] - 48;
            dist[i][j] = MAX_NUM;
        }
    }
    BFS();
    cout << dist[M-1][N-1] << endl;
    return 0;
}

/*
6 5
010001
010101
010101
010101
000100
-> 0

6 6
001111
010000
001111
110001
011010
100010
-> 2

4 2
0001
1000
-> 0

3 3
011
111
110
-> 3
*/

/*
6 5
010001
010101
010101
010101
000100
-> 0

6 6
001111
010000
001111
110001
011010
100010
-> 2

4 2
0001
1000
-> 0

3 3
011
111
110
-> 3
*/