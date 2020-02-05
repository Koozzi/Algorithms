#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<int> relation[1001];
int n, k;
int BFS(int start){
    queue<int> q;
    bool visited[1001] = {0};
    int depth[1001] = {0};
    int ans = 0;
    depth[start] = {0};
    visited[start] = true;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < relation[current].size() ; i++){
            int next = relation[current][i];
            if(!visited[next]){
                q.push(next);
                visited[next] = true;
                depth[next] = depth[current] + 1;
                ans += depth[next];
            }
        }
    }
    return ans;
}

int main(){
    cin >> n >> k;
    int min_rel = 1001;
    int min_idx = 0;
    for(int i = 0 ; i < k ; i++){
        int a, b;
        cin >> a >> b;
        relation[a].push_back(b);
        relation[b].push_back(a);
    }
    for(int i = 1 ; i < n+1 ; i++){
        int min_ans = BFS(i);
        if(min_ans < min_rel){
            min_rel = min_ans;
            min_idx = i;
        }
    }
    cout << min_idx << "\n";
    return 0;
}