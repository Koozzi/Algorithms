#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int N;
bool visit[25][25];
string map[25];
vector<int> Dangi;

struct Dir{
    int moveI, moveJ;
};
Dir moveDir[4] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void BFS(int startI, int startJ){
    int cnt = 1;
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visit[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI >= N || nextJ >= N || nextI < 0 || nextJ < 0) continue;

            if(!visit[nextI][nextJ] && map[nextI][nextJ] == '1'){
                q.push({nextI, nextJ});
                visit[nextI][nextJ] = true;
                cnt++;
            }
        }
    }
    Dangi.push_back(cnt);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> map[i];
    }

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == '1' && !visit[i][j]){
                BFS(i,j);
            }
        }
    }
    cout << Dangi.size() << "\n";
    sort(Dangi.begin(), Dangi.end());
    for(int i = 0 ; i < Dangi.size() ; i++){
        cout << Dangi[i] << "\n";
    }

    return 0;
}