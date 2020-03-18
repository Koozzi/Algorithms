#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int M;
int map[500][500];
int dp[500][500];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int move(int startI, int startJ){
    if(dp[startI][startJ] != 0){
        return dp[startI][startJ];
    }
    dp[startI][startJ] = 1;
    for(int i = 0 ; i < 4 ; i++){
        int nextI = startI + moveDir[i].moveI;
        int nextJ = startJ + moveDir[i].moveJ;
        if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
            if(map[startI][startJ] < map[nextI][nextJ]){
                dp[startI][startJ] = max(dp[startI][startJ], move(nextI, nextJ) + 1);
            }
        }
    }
    return dp[startI][startJ];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
        }
    }
    int ans = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            ans = max(ans, move(i,j));
        }
    }
    cout << ans << endl;
    return 0;
}