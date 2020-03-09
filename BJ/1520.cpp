#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int M, N;
int map[500][500];
bool visited[500][500];
typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
void show(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << visited[i][j] << " ";
        }cout << endl;
    }
}
void BFS(){
    vector<pair<int, int>> v;
    queue<pair<int, int>> q;
    q.push(make_pair(0,0));
    visited[0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] < map[currentI][currentJ]){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                }
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    BFS();
    show();
}