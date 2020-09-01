#include <iostream>
#include <string>
#include <queue>
using namespace std;

int N, M;
bool visit[100][100];
string map[100];

typedef struct{
    int moveI, moveJ;
} Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int BFS(){
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, 0});
    visit[0][0] = true;
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentD = q.front().second;
        if(currentI == N-1 && currentJ == M-1){
            return currentD;
        }
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= M) continue;

            if(!visit[nextI][nextJ] && map[nextI][nextJ] == '1'){
                q.push({{nextI, nextJ}, currentD + 1});
                visit[nextI][nextJ] = true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> map[i];
    }
    cout << BFS() + 1 << "\n";
    return 0;
}