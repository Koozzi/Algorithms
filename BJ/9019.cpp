#include <iostream>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

bool visited[10000];

void BFS(int startNode, int endNode){
    queue<pair<int, string>> q;
    q.push(make_pair(startNode, ""));
    visited[startNode] = true;
    while(!q.empty()){
        int c = q.front().first;
        string s = q.front().second;
        q.pop();

        if(c == endNode){
            cout << s << "\n";
            return;
        }

        int n;
        n = (c * 2) % 10000;
        if(!visited[n]){
            q.push(make_pair(n, s + "D"));
            visited[n] = true;
        }

        n = c - 1;
        if(n < 0){
            n = 9999;
        }
        if(!visited[n]){
            q.push(make_pair(n, s + "S"));
            visited[n] = true;
        }

        n = (c % 1000) * 10 + c / 1000;
        if(!visited[n]){
            q.push(make_pair(n, s + "L"));
            visited[n] = true;
        }

        n = (c % 10) * 1000 + c / 10;
        if(!visited[n]){
            q.push(make_pair(n, s + "R"));
            visited[n] = true;
        }   
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T; cin >> T;
    while(T--){
        int a, b;
        cin >> a >> b;
        memset(visited, false, sizeof(visited));
        BFS(a, b);
    }
    return 0;
}