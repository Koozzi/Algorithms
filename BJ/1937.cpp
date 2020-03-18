#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int M;
int map[500][500];
int dp[500][500]; 
void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cout << dp[i][j] << " ";
        }cout << endl;
    }
}
int DFS(int startI, int startJ){
    bool flag = false;
    vector<pair<int, int>> v;
    for(int i = 0 ; i < 4 ; i++){
        int nextI = startI + moveDir[i].moveI;
        int nextJ = startJ + moveDir[i].moveJ;
        if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < M){
            if(map[nextI][nextJ] > map[startI][startJ]){
                flag = true;
                dp[startI][startJ] = max(dp[startI][startJ], DFS(nextI, nextJ) + 1);
            }
        }
    }
    if(!flag){
        return 1;
    }
    else{
        return startD;
    }
}
int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
        }
    }
    int ans = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            ans = max(ans, DFS(i,j,1));
        }
    }
    cout << ans << endl;
    return 0;
}

/*
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
-> 4

2
1 1
1 1
-> 1

2
1 2
2 4
-> 3

5
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
-> 3

5
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
-> 3

5
3 3 3 4 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
-> 4

4 
14 9 12 10
1 11 5 4
10 15 4 5
9 8 7 6
-> 8
*/