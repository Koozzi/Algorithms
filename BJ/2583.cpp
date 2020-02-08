#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;

int M, N, K;

int map[100][100];
int visited[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void BFS(int startI, int startJ){
    int nodeCount = 1;
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
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && map[nextI][nextJ] == 0){
                    visited[nextI][nextJ] = true;
                    q.push({nextI, nextJ});
                    nodeCount++;
                }
            }
        }
    }
    v.push_back(nodeCount);
}

int main(){
    cin >> M >> N >> K;
    for(int i = 0 ; i < K ; i++){
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        for(int j = M - d ; j <= M - b - 1 ; j++){
            for(int k = a ; k <= c-1 ; k++){
                map[j][k] = 1;
            }
        }
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0 && !visited[i][j]){
                BFS(i,j);
            }
        }
    }
    sort(v.begin(), v.end());
    cout << v.size() << "\n";
    for(int i = 0 ; i < v.size() ; i++){
        cout << v[i] << " ";
    }
    cout << "\n";
    return 0;
}