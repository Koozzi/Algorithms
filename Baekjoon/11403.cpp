#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N, check;
int arr[101][10] = { 0 };

bool visited[101];

vector<int> connected[101];

int BFS(int I, int J){
    queue<int> q;
    check = 0;
    for(int i = 1 ; i < N+1 ; i++){
        visited[i] = false;
    }
    visited[I] = true;
    q.push(I);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < connected[current].size() ; i++){
            int next = connected[current][i];
            if(I == J && next == J){
                check = 1;
            if(!visited[next]){
                q.push(next);
                visited[next] = true;
                if(next == J){
                    check = 1;
                }
            }
        }
    }
    return check;
}

int main(){
    cin >> N;
    for(int i = 1 ; i < N+1 ; i++){
        for(int j = 1 ; j < N+1 ; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 1){
                connected[i].push_back(j);
            }
        }
    }
    for(int i = 1 ; i < N+1 ; i++){
        for(int j = 1 ; j < N+1 ; j++){
            cout << BFS(i, j) << " ";
        }
        cout << "\n";
    }
    return 0;
}