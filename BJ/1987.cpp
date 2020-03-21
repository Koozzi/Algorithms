#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, N, cnt = 0, ans = 1;
bool visited[26];
char map[21][21];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void DFS(int startI, int startJ){
    for(int i = 0 ; i < 4 ; i++){
        int nextI = startI + moveDir[i].moveI;
        int nextJ = startJ + moveDir[i].moveJ;
        if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
            if(!visited[map[nextI][nextJ] - 65]){
                visited[map[nextI][nextJ] - 65] = true;
                cnt++;
                ans = max(ans, cnt);
                DFS(nextI, nextJ);
                visited[map[nextI][nextJ] - 65] = false;
                cnt--;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }

    visited[map[0][0] - 65] = true;
    cnt = 1;

    DFS(0,0);

    cout << ans << endl;

    return 0;
}

/*
2 4
CAAB
ADCB
-> 3

2 4
AAAA
AAAA
-> 1

2 4
AAAA
BCDE
-> 5

1 1
A
-> 1
*/