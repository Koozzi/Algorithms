#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int M, N, map[1000][1000];
bool visited[1000][1000];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

queue<pair<pair<int, int>, int>> q;

int BFS(){
    int ans = 0;
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentD = q.front().second;
        q.pop();

        ans = max(ans, currentD);

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            
            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] == 0){
                q.push({{nextI, nextJ}, currentD + 1});
                visited[nextI][nextJ] = true;
                map[nextI][nextJ] = 1;
            }
        }
    }

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0){
                return -1;
            }
        }
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
            if(map[i][j] == 1){
                q.push({{i,j} ,0});
                visited[i][j] = true;
            }
        }
    }

    cout << BFS() << "\n";
    return 0;
}