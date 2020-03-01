#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int a, b, c, d, e;

int floor[1000001];
int depth[1000001];
bool visited[1000001];

void BFS(){
    queue<int> q;
    q.push(b);
    visited[b] = true;
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < 2 ; i++){
            int next;
            if(i == 0){
                next = current + d;
            }
            else{
                next = current - e;
            }
            if(next >= 1 && next <= a){
                if(!visited[next]){
                    q.push(next);
                    visited[next] = true;
                    depth[next] = depth[current] + 1;
                }
            }
        }
    }
    if(visited[c]){
        cout << depth[c] << "\n";
    }
    else{
        cout << "use the stairs" << "\n";
    }
}

int main(){
    cin >> a >> b >> c >> d >> e;
    BFS();
    return 0;
}