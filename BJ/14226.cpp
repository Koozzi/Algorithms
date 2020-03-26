#include <iostream>
#include <queue>

using namespace std;

int M;
bool visited[1001][1001];

void BFS(){
    queue<pair<pair<int, int>, int>> q;
    q.push(make_pair(make_pair(1,0), 0));
    visited[1][0] = true;
    while(!q.empty()){
        int disp = q.front().first.first;
        int clip = q.front().first.second;
        int time = q.front().second;
        q.pop();

        if(disp == M){
            cout << time << "\n";
            return;
        }

        if(disp > 0 && disp < 1001){
            if(!visited[disp][disp]){ // 복사 
                q.push(make_pair(make_pair(disp, disp), time + 1));
                visited[disp][disp] = true;
            }

            if(!visited[disp-1][disp]){ // 삭제
                q.push(make_pair(make_pair(disp - 1, clip), time + 1));
                visited[disp-1][disp] = true;
            }
        }

        if(clip > 0 && clip + disp < 1001){// 붙여넣기
            if(!visited[clip + disp][clip]){
                q.push(make_pair(make_pair(clip + disp, clip), time + 1));
            }
        }

    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;   

    BFS();
    
    return 0;
}