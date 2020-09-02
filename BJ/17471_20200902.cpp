#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int N, arr[11], ans = 98765432;
bool visit[11];
bool BFSvisit[11];
bool canDivide;
vector<int> relation[11];
vector<int> t1;
vector<int> t2;

bool checkGoodTeam(int start){
    for(int i = 1 ; i <= N ; i++){
        BFSvisit[i] = false;
    }
    bool isTeamOne = (start == t1[0]);
    int cnt = 1;
    queue<int> q;
    q.push(start);
    BFSvisit[start] = true;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < relation[c].size() ; i++){
            int n = relation[c][i];
            if(visit[c] == visit[n] && !BFSvisit[n]){
                q.push(n);
                BFSvisit[n] = true;
                cnt++;
            }
        }
    }
    if(isTeamOne){
        if(cnt != t1.size()) return false;
    }
    else{
        if(cnt != t2.size()) return false;
    }
    return true;
}

bool checkGoodDivide(){
    for(int i = 1 ; i <= N ; i++){
        if(!visit[i]) t2.push_back(i);
    }
    if(t1.size() == 0 || t2.size() == 0){
        t2.clear();
        return false;
    }

    if(checkGoodTeam(t1[0]) && checkGoodTeam(t2[0])){
        return true;
    }
    t2.clear();
    return false;
}

int getScore(){
    int t1Score = 0;
    int t2Score = 0;
    for(int i = 0 ; i < t1.size() ; i++){
        t1Score += arr[t1[i]];
    }
    for(int i = 0 ; i < t2.size() ; i++){
        t2Score += arr[t2[i]];
    }
    return abs(t1Score - t2Score);
}

void DFS(int start){
    if(checkGoodDivide()){
        canDivide = true;
        ans = min(ans, getScore());
        t2.clear();
    }
    for(int i = start + 1 ; i <= N ; i++){
        if(!visit[i]){
            t1.push_back(i);
            visit[i] = true;
            DFS(i);
            visit[i] = false;
            t1.pop_back();
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        cin >> arr[i];
    }
    for(int i = 1 ; i <= N ; i++){
        int a; cin >> a;
        for(int j = 0 ; j < a ; j++){
            int b; cin >> b;
            relation[i].push_back(b);
        }
    }
    DFS(0);
    if(canDivide) cout << ans << "\n";
    if(!canDivide) cout << -1 << "\n";
    return 0;
}