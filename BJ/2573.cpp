#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int M, N, check, mapSum;
int map[301][301];
bool visited[301][301];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void melt(){    
    int afterMelt[301][301];
    mapSum = 0;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            afterMelt[i][j] = map[i][j];
        }
    }
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            if(map[i][j]){
                for(int k = 0 ; k < 4 ; k++){
                    int nextI = i + moveDir[k].moveI;
                    int nextJ = j + moveDir[k].moveJ;
                    if(nextI >= 1 && nextI <= M && nextJ >= 1 && nextJ <=N){
                        if(!map[nextI][nextJ]){
                            afterMelt[i][j]--;
                            if(afterMelt[i][j] < 0){
                                afterMelt[i][j] = 0;
                            }
                        }
                    }
                }
            }
        }
    }
     
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            map[i][j] = afterMelt[i][j];
            mapSum += map[i][j];
        }
    }
}

void BFS(int startI, int startJ){
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
            if(nextI >= 1 && nextI <= M && nextJ >= 1 && nextJ <= N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ]){
                    q.push({nextI, nextJ});
                    visited[nextI][nextJ] = true;
                }
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> map[i][j];
        }
    }
    memset(visited, false, sizeof(visited));
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            if(map[i][j] && !visited[i][j]){
                BFS(i, j);
                check++;
            }
        }
    }
    if(check >= 2){
        cout << 0 << "\n";
    }
    else{
        int dayCount = 0;
        while(1){
            memset(visited, false, sizeof(visited));
            dayCount++;
            melt();
            check = 0;
            for(int i = 1 ; i <= M ; i++){
                for(int j = 1 ; j <= N ; j++){
                    if(map[i][j] && !visited[i][j]){
                        BFS(i, j);
                        check++;
                    }
                }
            }
            if(check >= 2){
                cout << dayCount << "\n";
                break;
            }
            if(mapSum == 0){
                cout << 0 << "\n";
                break;
            }
        }
    }
    return 0;
}
