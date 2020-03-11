#include <iostream>
#include <deque>

using namespace std;

int M, N;
char inputData[1001][1001];
int map[1000][1000];
bool visitied[1000][1000][2];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void BFS(){
    deque<pair<pair<int, int>, pair<int, int>>> dq;
    dq.push_back(make_pair(make_pair(0,0), make_pair(0,1)));
    visitied[0][0][0] = true;
    while(!dq.empty()){
        int currentI = dq.front().first.first;
        int currentJ = dq.front().first.second;
        int currentB = dq.front().second.first;
        int currentD = dq.front().second.second;
        dq.pop_front();
        if(currentI == M-1 && currentJ == N-1){
            cout << currentD << endl;
            return;
        }
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveDir[i].moveI;
            int nextJ = currentJ + moveDir[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(map[nextI][nextJ] == 1 && currentB == 0){
                    dq.push_back(make_pair(make_pair(nextI, nextJ), make_pair(currentB + 1, currentD + 1)));
                    visitied[nextI][nextJ][currentB + 1] = true;
                }
                else if(map[nextI][nextJ] == 0 && !visitied[nextI][nextJ][currentB]){
                    dq.push_back(make_pair(make_pair(nextI, nextJ), make_pair(currentB, currentD + 1)));
                    visitied[nextI][nextJ][currentB] = true;
                }
            }
        }
    }
    cout << -1 << endl;
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> inputData[i];
        for(int j = 0 ; j < N ; j++){
            map[i][j] = int(inputData[i][j] - 48);
        }
    }
    BFS();
    return 0;
}

/*
6 4
0100
1110
1000
0000
0111
0000
Answer : 15

4 4
0111
1111
1111
1110
Answer : -1
*/