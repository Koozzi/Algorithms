#include <iostream>
#include <queue>
#include <string>
using namespace std;

int M, N;
bool visited[1000][1000][2];
string map[1000];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int BFS(){
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{0,0},{1,0}});
    visited[0][0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first.first; 
        int currentJ = q.front().first.second;
        int depth = q.front().second.first;
        int cnt = q.front().second.second;
        q.pop();

        if(currentI == M-1 && currentJ == N-1){
            return depth;
        }

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextJ < 0 || nextI >= M || nextJ >= N){
                continue;
            }

            if(map[nextI][nextJ] == '1' && cnt == 0){
                q.push({{nextI, nextJ}, {depth+1, cnt+1}});
                visited[nextI][nextJ][cnt+1] = true;
            }
            else if(map[nextI][nextJ] == '0' && !visited[nextI][nextJ][cnt]){
                q.push({{nextI, nextJ}, {depth+1, cnt}});
                visited[nextI][nextJ][cnt] = true;
            }
        }
    }
    return -1;
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