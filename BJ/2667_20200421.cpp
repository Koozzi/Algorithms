#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int M;
bool visited[25][25];
string map[25];
vector<int> ans;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int BFS(int startI, int startJ){
    int cnt = 0; 
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    visited[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        cnt++;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;

            if(nextI < 0 || nextI >= M || nextJ < 0 || nextJ >= M) continue;

            if(!visited[nextI][nextJ] && map[nextI][nextJ] == '1'){
                q.push({nextI, nextJ});
                visited[nextI][nextJ] = true;
            }
        }
    }
    return cnt;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }
    
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            if(map[i][j] == '1' && !visited[i][j]){
                ans.push_back(BFS(i,j));
            }
        }
    }
    sort(ans.begin(), ans.end());
    
    cout << ans.size() << "\n";
    for(int i = 0 ; i < ans.size() ; i++){
        cout << ans[i] << "\n";
    }

    return 0;
}  