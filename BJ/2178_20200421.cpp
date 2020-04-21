#include <iostream>
#include <queue>
#include <string>
using namespace std;

int M, N;
bool visited[100][100];
string map[100];
typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};


int BFS(){
    queue<pair<pair<int, int>, int>> q;
    q.push({{0,0}, 1});
    visited[0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentD = q.front().second;
        q.pop();

        if(currentI == M - 1 && currentJ == N - 1){
            return currentD;
        }
        
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] == '1'){
                q.push({{nextI, nextJ}, currentD + 1});
                visited[nextI][nextJ] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }

    cout << BFS() << "\n";
    return 0;
}