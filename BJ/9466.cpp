#include <iostream>
#include <queue>
#include <cstring>
#include <vector>
#define MAX_NUM 100001
using namespace std;

int M, T;
int dest[MAX_NUM];
bool cycle[MAX_NUM];
bool visited[MAX_NUM];
vector<int> sour[MAX_NUM];

void goBack(int start){
    queue<int> q;
    q.push(start);
    visited[start] = false;
    while(!q.empty()){
        int c = q.front();
        cycle[c] = true;
        q.pop();
        for(int i = 0 ; i < sour[c].size() ; i++){
            int n = sour[c][i];
            if(visited[n]){
                q.push(n);
                visited[n] = false;
            }
        }
    }
}

void BFS(int start){
    memset(visited, false, sizeof(visited));
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int c = q.front();
        int n = dest[c];
        q.pop();
        if(!visited[n]){
            q.push(n);
            visited[n] = true;
        }
        else{
            if(n == start){
                goBack(n);
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    while(T--){
        cin >> M;
        for(int i = 1; i <= M ; i++){
            cin >> dest[i];
            sour[dest[i]].push_back(i);
        }

        for(int i = 1 ; i <= M ; i++){
            if(!cycle[i]) BFS(i);
        }

        int ans = 0 ;
        for(int i = 1 ; i <= M ; i++){
            if(!cycle[i]) ans++;
        }

        cout << ans << "\n";
        for(int i = 1 ; i <= M ; i++){
            sour[i].clear();
        }
    }
}