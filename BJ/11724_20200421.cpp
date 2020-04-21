#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int M, N, ans;
bool visited[1001];
vector<int> v[1001];

void initset(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(!visited[n]){
                q.push(n);
                visited[n] = true;
            }
        }
    }
}

int main()
{
    initset();
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i = 1 ; i <= M ; i++){
        if(!visited[i]){
            BFS(i);
            ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}