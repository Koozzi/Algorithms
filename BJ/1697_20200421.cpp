#include <iostream>
#include <queue>
#include <algorithm>
#define MAX_NUM 100001
#define INIT_NUM 987665432
using namespace std;

int M, N;
int visited[MAX_NUM];

void init(){
    for(int i = 0 ; i <= MAX_NUM ; i++){
        visited[i] = INIT_NUM;
    }
}

int BFS(){
    queue<int> q;
    q.push(M);
    visited[M] = 0;
    while(!q.empty()){
        int c = q.front();
        int n = 0;
        q.pop();

        if(c == N){
            return visited[c];
        }

        n = c * 2;
        if(n < MAX_NUM){
            if(visited[n] > visited[c] + 1){
                q.push(n);
                visited[n] = visited[c] + 1;
            }
        }

        n = c + 1;
        if(n < MAX_NUM){
            if(visited[n] > visited[c] + 1){
                q.push(n);
                visited[n] = visited[c] + 1;
            }
        }

        n = c - 1;
        if(n >= 0){
            if(visited[n] > visited[c] + 1){
                q.push(n);
                visited[n] = visited[c] + 1;
            }
        }
    }
}

int main(){
    init();
    cin >> M >> N;
    cout << BFS() << "\n";
    return 0;
}