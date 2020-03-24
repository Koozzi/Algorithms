#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define MAX_NUM 99900000

using namespace std;

vector<pair<int, int>> v[1001];
int M, N, S, E;
int dp[1001];

void dijkstra(int start, int end){
    memset(dp, MAX_NUM, sizeof(dp));
    queue<int> q;
    q.push(start);
    dp[start] = 0;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i].first;
            if(dp[n] > dp[c] + v[c][i].second){
                dp[n] = dp[c] + v[c][i].second;
                q.push(n);
            }
        }
    }
    cout << dp[end] << endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back(make_pair(b,c));
    }
    cin >> S >> E;
    dijkstra(S, E);
    return 0;
}