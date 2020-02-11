#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

typedef struct{
    int moveI, moveJ, moveK;
}Dir;
Dir moveDir[6] = {{1, 0, 0}, {-1, 0, 0}, {0, 0, 1}, {0, 0, -1}, {0, 1, 0}, {0, -1, 0}};

char map[31][31][31];
bool visited[30][30][30];
int depth[30][30][30];

int K, I, J;
int endK, endI, endJ;

bool BFS(int startK, int startI, int startJ){
    memset(visited, false, sizeof(visited));
    memset(depth, 0 , sizeof(depth));
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{startK, startI}, {startJ, 0}});
    visited[startK][startI][startJ] = true;
    while(!q.empty()){
        int currentK = q.front().first.first;
        int currentI = q.front().first.second;
        int currentJ = q.front().second.first;
        q.pop();
        for(int i = 0 ; i < 6 ; i++){
            int nextK = currentK + moveDir[i].moveK;
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextK >= 0 && nextK < K && nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J){
                if(!visited[nextK][nextI][nextJ] && map[nextK][nextI][nextJ] != '#'){
                    q.push({{nextK, nextI}, {nextJ, 0}});
                    visited[nextK][nextI][nextJ] = true;
                    depth[nextK][nextI][nextJ] = depth[currentK][currentI][currentJ] + 1;
                }
            }
        }
    }
    if(depth[endK][endI][endJ] != 0){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    while(1){
        int startK, startI, startJ;
        cin >> K >> I >> J;
        if(K == 0 && I == 0 && J == 0){
            break;
        }
        for(int k = 0 ; k < K ; k++){
            for(int i = 0 ; i < I ; i++){
                for(int j = 0 ; j < J ; j++){
                    char inputData[31];
                    cin >> inputData[j];
                    map[k][i][j] = inputData[j];
                    if(map[k][i][j] == 'S'){
                        startK = k;
                        startI = i;
                        startJ = j;
                    }
                    if(map[k][i][j] == 'E'){
                        endK = k;
                        endI = i;
                        endJ = j;
                    }
                }
            }
        }
        if(BFS(startK, startI, startJ)){
            printf("Escaped in %d minute(s).\n", depth[endK][endI][endJ]);
        }
        else{
            cout << "Trapped!" << "\n";
        }
    }
    return 0;
}
