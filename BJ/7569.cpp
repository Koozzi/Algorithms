#include <iostream>
#include <queue>

using namespace std;

typedef struct{
    int moveI, moveJ, moveK;
}Dir;
Dir moveDir[6] = {{0, 0, 1}, {0, 0, -1}, {-1, 0, 0}, {1, 0, 0}, {0, 1, 0}, {0, -1, 0}};

int tomato[100][100][100];
int depth[100][100][100] = {0};
bool visited[100][100][100];

int I, J, K;

int BFS(){
    queue<pair< pair<int, int>, pair<int, int>> > q;
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            for(int k = 0 ; k < K ; k++){
                if(tomato[i][j][k] == 1){
                    visited[i][j][k] = true;
                    q.push({{i,j}, {k,0}});
                }
            }
        }
    }

    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentK = q.front().second.first;
        q.pop();
        for(int i = 0 ; i < 6 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            int nextK = currentK + moveDir[i].moveK;
            if(nextI >= 0 && nextI < I && nextJ >= 0 && nextJ < J && nextK >= 0 && nextK < K){
                if(!visited[nextI][nextJ][nextK] && tomato[nextI][nextJ][nextK] == 0){
                    q.push({{nextI, nextJ}, {nextK, 0}});
                    visited[nextI][nextJ][nextK] = true;
                    depth[nextI][nextJ][nextK] = depth[currentI][currentJ][currentK] + 1;
                    tomato[nextI][nextJ][nextK] = 1;
                }
            }
        }
    }

    int longestDay = 0;
    for(int i = 0 ; i < I ; i++){
        for(int j = 0 ; j < J ; j++){
            for(int k = 0 ; k < K ; k++){
                if(depth[i][j][k] >= longestDay){
                    longestDay = depth[i][j][k];
                }
                if(tomato[i][j][k] == 0){
                    return -1;
                }
            }
        }
    }
    return longestDay;
}

int main(){
    int zeroCount = 0;
    int oneCount = 0;
    cin >> J >> I >> K;
    // I : 가로 , J : 세로 , K : 높이
    for(int k = 0 ; k < K ; k++){
        for(int i = 0 ; i < I ; i++){
            for(int j = 0 ; j < J ; j++){
                cin >> tomato[i][j][k];
                if(tomato[i][j][k] == 1){
                    oneCount++;
                }
                else if(tomato[i][j][k] == 0){
                    zeroCount++;
                }
            }
        }
    }
    if(zeroCount == 0 || oneCount == 0){
        cout << 0 << "\n";
    }
    else{
        cout << BFS() << "\n";    
    }

    return 0;
}

/*
문제를 푸는데 시간이 오래 걸린 이유
1. 3차원 배열을 입력 받을 때 i 와 j 를 헷갈림
    5 3 2 를 입력받으면 i : 3, j : 5, k : 2 로 받아야 하는데
                    i : 5, j : 3, k : 2 로 입력을 받음.

배운 점
queue 를 사용하는데 항상 queue<pair<int, int>> 만 사용했었음
이 것은 2개의 쌍을 가질 때 사용했는데
3개의 쌍이 필요할 때는
queue<pair<pair<int, int>, pair<int, int>>> 로 2개의 pair를 쌍으로 해서 받음
마지막 하나는 그냥 0으로 항상 때려박으면 됨
*/