#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int N, M, ans=2e9;
int moveI[4] = {0, 0, 1, -1};
int moveJ[4] = {1, -1, 0, 0};
int map[50][50];
bool visit[50][50], used[10];

vector<pair<int, int>> v;

int BFS(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            visit[i][j] = false;
        }
    }

    int depth[50][50] = {0,};
    char copy_map[50][50];

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0){
                copy_map[i][j] = '0';
            }
            else if(map[i][j] == 2){
                copy_map[i][j] = '*';
            }
            else{
                copy_map[i][j] = '-';
            }
        }
    }

    queue<pair<int, int>> q;
    for(int i = 0 ; i < 10 ; i++){
        if(used[i]){
            int I = v[i].first;
            int J = v[i].second;
            q.push({I, J});
            visit[I][J] = true;
            copy_map[I][J] = '#';
        }
    }

    while(!q.empty()){
        int currentI = q.front().first;
        int currentJ = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveI[i];
            int nextJ = currentJ + moveJ[i];
            
            if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= N) continue;
            if (visit[nextI][nextJ]) continue;

            if(copy_map[nextI][nextJ] == '0' || copy_map[nextI][nextJ] == '*'){
                q.push({nextI, nextJ});
                depth[nextI][nextJ] = depth[currentI][currentJ] + 1;
                visit[nextI][nextJ] = true;
                copy_map[nextI][nextJ] = 'X';
            }
        }
    }

    bool spread_all = true;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(copy_map[i][j] == '0'){
                spread_all = false;
            }
        }
    }

    if(!spread_all){
        return ans;
    }

    int max_depth = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 0){
                max_depth = max(max_depth, depth[i][j]);
            }
        }
    }
    return max_depth;
}

void get_virus(int cnt, int start){
    if(cnt == M){
        ans = min(ans, BFS());
    }
    for(int i = start + 1 ; i < v.size() ; i++){
        if(used[i]) continue;
        used[i] = true;
        get_virus(cnt+1, i);
        used[i] = false;    
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
            if(map[i][j] == 2){
                v.push_back({i,j});
            }
        }
    }
    
    get_virus(0, -1);
    if(ans == 2e9) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}