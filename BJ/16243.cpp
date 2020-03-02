#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

int M, L, R;
int changeCount = 0;
int map[50][50];
bool visited[50][50];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void setSection(int startI, int startJ){
    changeCount = 0;
    queue<pair<int, int>> q;
    vector<pair<int, int>> v;
    q.push(make_pair(startI, startJ));
    v.push_back(make_pair(startI, startJ));
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
                if(!visited[nextI][nextJ]){
                    int gap = abs(map[currentI][currentJ] - map[nextI][nextJ]);
                    if(gap >= L && gap <= R){
                        q.push(make_pair(nextI, nextJ));
                        v.push_back(make_pair(nextI, nextJ));
                        visited[nextI][nextJ] = true;
                        changeCount++;
                    }
                }
            }
        }
    }
    int sum = 0;
    for(int i = 0 ; i < v.size() ; i++){
        sum += map[v[i].first][v[i].second];
    }
    int avg = sum / v.size();
    for(int i = 0 ; i < v.size() ; i++){
        map[v[i].first][v[i].second] = avg;
    }
}

int main(){
    cin >> M >> L >> R;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
        }
    }
    for(int T = 0 ; T < 2000 ; T++){
        int ansCount = 0;
        memset(visited, false, sizeof(visited));
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                if(!visited[i][j]){
                    setSection(i,j);
                    ansCount += changeCount;
                }
            }
        }
        if(ansCount == 0){
            cout << T << "\n";
            return 0;
        }        
    }
}