#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

vector<char> puyo[6];
char map[13][7];
bool visited[6][12];
int check;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void BFS(int startI, int startJ){
    char tmp = puyo[startI][startJ];
    vector<pair<int, int>> v;
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    puyo[startI][startJ] = 'X';
    visited[startI][startJ] = true;
    v.push_back(make_pair(startI, startJ));
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < 6 && nextJ >= 0 && nextJ < 12){
                if(puyo[nextI][nextJ] != 'X' && puyo[nextI][nextJ] == tmp){
                    q.push({nextI, nextJ});
                    visited[nextI][nextJ] = true;
                    puyo[nextI][nextJ] = 'X';
                    v.push_back(make_pair(nextI, nextJ));
                }
            }
        }
    }
    if(v.size() < 4){
        for(int i = 0 ; i < v.size() ; i++){
            int a = v[i].first;
            int b = v[i].second;
            puyo[a][b] = tmp;
        }
    }
}

int main(){
    for(int i = 0 ; i < 12 ; i++){
        cin >> map[i];
    }
    
    for(int j = 0 ; j < 6 ; j++){
        for(int i = 11 ; i >= 0 ; i--){
            puyo[j].push_back(map[i][j]);
        }
    }
    int ans = 0;
    while(1){
        int xCount = 0 ;
        memset(visited, false, sizeof(visited));
        for(int i = 0 ; i < 6 ; i++){
            for(int j = 0 ; j < 12 ; j++){
                if(!visited[i][j] && puyo[i][j] != '.' && puyo[i][j] != 'X'){
                    BFS(i, j);
                }
            }
        }
        for(int i = 0 ; i < 6 ; i++){
            for(int j = 0 ; j < 12 ; j++){
                if(puyo[i][j] == 'X'){
                    xCount++;
                }
            }
        }
        if(xCount == 0){
            break;
        }
        for(int i = 0 ; i < 6 ; i++){
            for(int j = 0 ; j < 12 ; j++){
                if(puyo[i][j] == 'X'){
                    puyo[i].erase(puyo[i].begin() + j);
                    puyo[i].push_back('.');
                    j--;
                }
            }
        }
        ans++;
    }
    cout << ans << "\n";
    return 0;
}

/*
vector.erase(erase.begin() + "지우고 싶은 원소 idx");
vector[a].erase(erase[a].begin() + "지우고 싶은 원소 idx");
*/