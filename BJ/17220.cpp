#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> give[27];
vector<int> arrest;

int M, N, arrestNum;
bool visited[27];
int Xcount = 0;

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < give[current].size() ; i++){
            int next = give[current][i];
            if(!visited[next]){
                printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
                q.push(next);
                visited[next] = true;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        char a, b;
        cin >> a >> b;
        give[int(a) - 65].push_back(int(b) - 65);
    }
    cin >> arrestNum;
    for(int i = 0 ; i < arrestNum ; i++){
        char a;
        cin >> a;
        arrest.push_back(int(a) - 65);
    }
    for(int i = 0 ; i < arrest.size() ; i++){
        if(!visited[arrest[i]]){
            BFS(arrest[i]);
        }
    }
    if(visited[0]){
        cout << 0 << "\n";
        return 0;
    }
    else{
        for(int i = 1 ; i < M ; i++){
            if(!visited[i]){
                Xcount++;
            }
        }
        cout << Xcount << "\n";
        return 0;
    }
}