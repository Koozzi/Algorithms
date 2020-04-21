#include <iostream>
#include <queue>
#include <string>
#define INIT_NUM 98765432
using namespace std;

int M, N;
int ans[100][100];
string map[100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int BFS(){
    queue<pair<int, int>> q;
    q.push({0,0});
    ans[0][0] = 0;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();

        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= N) continue;

            int var = ans[currentI][currentJ] + map[nextI][nextJ] - '0';

            if(var < ans[nextI][nextJ]){
                q.push({nextI, nextJ});
                ans[nextI][nextJ] = var;
            }
        }
    }
    return ans[M-1][N-1];
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            ans[i][j] = INIT_NUM;
        }
    }

    cout << BFS() << "\n";
    return 0;
}