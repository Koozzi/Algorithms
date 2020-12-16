#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int M, N, ans, cnt;
int map[100][100];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void BFS(){
    queue<pair<int, int>> q;
    q.push({0,0});
    map[0][0] = 8;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            
            if(nextI >= M && nextJ >= N && nextI < 0 && nextJ < 0) continue;

            if(map[nextI][nextJ] == 0){
                q.push({nextI, nextJ});
                map[nextI][nextJ] = 8;
            }
        }
    }
}

int getSize(){
    int count = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 1){
                count++;
            }
        }
    }
    return count;
}

void deleteBoundary(){
    vector<pair<int, int>> v;
    for(int i = 1 ; i < M-1 ; i++){
        for(int j = 1 ; j < N-1 ; j++){
            if(map[i-1][j] == 0 || map[i+1][j] == 0 || map[i][j-1] == 0 || map[i][j+1] == 0){
                v.push_back({i,j});
            }
        }
    }

    for(int i = 0 ; i < v.size() ; i++){
        map[v[i].first][v[i].second] = 0;
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }

    while(1){
        // 1. 녹는 부분 파악
        // 2. 녹기전 치즈 크기 파악
        // 3. 녹이기
        // 4. 다 녹았는지 체크

        // BFS(); // 녹는 부분 파악하기

        cout << "---------------------" << "\n";
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                cout << map[i][j] << " ";
            }cout << "\n";
        }
        cout << "---------------------" << "\n";

        ans = getSize();
        deleteBoundary();
        cnt++;

        if(getSize() == 0){
            cout << cnt << "\n";
            cout << ans << "\n";
            return 0;
        }
    }
}