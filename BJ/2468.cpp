#include <iostream>
#include <queue>

using namespace std;

int M, r;

int map[100][100];
bool visited[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,1}, {0,-1}};

void BFS(int startI, int startJ){ 
    queue<pair<int ,int>> q;
    q.push({startI, startJ});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
                if(!visited[nextI][nextJ]
                && map[nextI][nextJ] > r){
                    q.push({nextI, nextJ});
                    visited[nextI][nextJ] = true;
                }
            }
        }
    }
}

int main(){
    int highest = 0;
    
    cin >> M;
    
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
            if(map[i][j] >= highest){
                highest = map[i][j];
            }
        }
    }
    
    int ans = 0;
    
    for(r = 0 ; r <= highest ; r++){
        int safeSection = 0;
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                if(map[i][j] > r && !visited[i][j]){
                    BFS(i,j);
                    safeSection++;
                }
            }
        }
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                visited[i][j] = false;
            }
        }
        if(safeSection >= ans){
            ans = safeSection;
        }
    }
    cout << ans << "\n";
    return 0;
}

/*
문제를 푸는데 시간이 오래 걸린 이유
visited 배열을 초기화를 해야되는데 
어느 위치에서 초기화를 해야하는지 헷갈렸다. 

다음에 문제를 풀 때는 배열 visited 배열 초기화에 조금 더 신경을 쓸 것!
*/