#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,1}, {0,-1}};

int depth[50][50];
char map[51][51];
bool visited[50][50];

int I, J;

int BFS(int startI, int startJ){
    memset(visited, false, sizeof(visited));
    memset(depth, 0, sizeof(depth));
    int deep = 0;
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == 'L'){
                    q.push({nextI, nextJ});
                    visited[nextI][nextJ] = true;
                    depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                    if(depth[nextI][nextJ] > deep){
                        deep = depth[nextI][nextJ];
                    }
                }
            }
        }
    }
    return deep;
}

int main(){
    int longest = 0;
    cin >> I >> J;
    for(int i = 0 ; i < I ; i++){
        cin >> map[i];
    }
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
            if(map[i][j] == 'L'){
                if(BFS(i, j) >= longest){
                    longest = BFS(i, j);
                }
            }
        }
    }
    cout << longest << "\n"
    ;
    return 0;
}