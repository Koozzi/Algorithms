#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int M, N;

char map[51][51];
int depth[50][50];
bool visited[50][50];

int keyCount[6];
typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

vector<pair<pair<int, int>, int>> v; 
vector<pair<int, int>> door[6];
vector<pair<int, int>> EXIT;
vector<vector<pair<int, int>>> route;
bool keySum(){
    int sum = 0;
    for(int i = 0 ; i < 6 ; i++){
        sum += keyCount[i];
    }
    if(sum == 0){
        return false;
    }
    else{
        return true;
    }
}
void show(){
    cout << "\n";
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j];
        }cout << "\n";
    }
}
void openDoor(){
    for(int t = 0 ; t < 6 ; t++){
        if(keyCount[t] != 0){
            printf("%d open\n", t);
            for(int i = 0 ; i < door[t].size() ; i++){
                map[door[t][i].first][door[t][i].second] = '.';
            }   
        }
    }
}
bool BFS(int startI, int startJ){
    memset(visited, false, sizeof(visited));
    memset(depth, 0, sizeof(depth));
    queue<pair<int, int>> q;
    q.push(make_pair(startI, startJ));
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ] && (map[nextI][nextJ] == '.'
                || map[nextI][nextJ] == '1'
                || (int(map[nextI][nextJ]) >= 97 
                && int(map[nextI][nextJ]) <= 102)) ){
                    q.push(make_pair(nextI, nextJ));
                    visited[nextI][nextJ] = true;
                    depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                    for(int t = 0 ; t < 6 ; t++){
                        if(map[nextI][nextJ] == char(t + 97)){
                            map[nextI][nextJ] = '.';
                            if(keyCount[t] == 0){
                                keyCount[t]++;
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
    for(int i = 0 ; i < EXIT.size() ; i++){
        if(visited[EXIT[i].first][EXIT[i].second]){
            return true;
        }
    }
    return false;
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == '0'){
                v.push_back(make_pair(make_pair(i,j), 0));
            }
            else if(map[i][j] == 'A'){
                door[0].push_back(make_pair(i,j));
            }
            else if(map[i][j] == 'B'){
                door[1].push_back(make_pair(i,j));
            }
            else if(map[i][j] == 'C'){
                door[2].push_back(make_pair(i,j));
            }
            else if(map[i][j] == 'D'){
                door[3].push_back(make_pair(i,j));
            }
            else if(map[i][j] == 'E'){
                door[4].push_back(make_pair(i,j));
            }
            else if(map[i][j] == 'F'){
                door[5].push_back(make_pair(i,j));
            }
            else if(map[i][j] == '1'){
                EXIT.push_back(make_pair(i,j));
            }
        }
    }

    BFS(v[0].first.first, v[0].first.second);
    openDoor();
    show();
    
    return 0;
}