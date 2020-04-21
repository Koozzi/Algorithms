#include <iostream>
#include <queue>
#define INIT_NUM 98765432;
using namespace std;

int M;
int visited[1001][1001];

void init(){
    for(int i = 0 ; i <= 1000 ; i++){
        for(int j = 0 ; j <= 1000 ; j++){
            visited[i][j] = INIT_NUM;
        }
    }
}

int BFS(){
    queue<pair<pair<int, int>, int>> q;
    q.push({{1, 0}, 0});
    visited[1][0] = 0;
    while(!q.empty()){
        int disp = q.front().first.first;
        int clip = q.front().first.second;
        int time = q.front().second;
        q.pop();

        // printf("%d / %d / %d\n", disp, clip, time);

        if(disp == M){
            return time;
        }

        q.push({{disp, disp}, time + 1});
        visited[disp][disp] = time + 1;
         // 복사

        if(disp + clip < 1001){
            if(visited[disp + clip][clip] > time + 1){
                q.push({{disp + clip, clip}, time + 1});
                visited[disp + clip][clip] = time + 1;
            }
        } // 붙여넣기

        if(disp - 1 >= 0){
            if(visited[disp-1][clip] > time + 1){
                q.push({{disp - 1, clip}, time + 1});
                visited[disp - 1][clip] = time + 1;
            }
        } // 삭제
    }
}

int main(){
    init();
    cin >> M;
    cout << BFS() << "\n";
    return 0;
}
