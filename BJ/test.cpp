#include <iostream>
#include <deque>

using namespace std;

int K, M, N;
int ans = 999999;
int map[200][200];
int visited[200][200][31];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveMonkey[4] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
Dir moveHorse[8] = {{-2,-1}, {-2,1}, {-1,2}, {1,2}, {2,1}, {2,-1}, {1,-2}, {-1,-2}};

void BFS(){
    deque<pair<pair<int, int>, pair<int, int>>> dq;
    dq.push_back(make_pair(make_pair(0,0), make_pair(0,0)));
    visited[0][0][0] = true;
    while(!dq.empty()){
        int currentI = dq.front().first.first;
        int currentJ = dq.front().first.second;
        int currentH = dq.front().second.first;
        int currentD = dq.front().second.second;
        dq.pop_front();
        if(currentI == M-1 && currentJ == N-1){
            cout << currentD << endl;
            return;
        }
        if(currentH < K){
            for(int i = 0 ; i < 8 ; i++){
                int nextI = currentI + moveHorse[i].moveI;
                int nextJ = currentJ + moveHorse[i].moveJ;
                int nextH = currentH + 1;
                if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                    if(!visited[nextI][nextJ][nextH] && map[nextI][nextJ] != 1){
                        dq.push_back(make_pair(make_pair(nextI, nextJ), make_pair(nextH, currentD + 1)));
                        visited[nextI][nextJ][nextH] = true;
                    }
                }
            }
        }
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + moveMonkey[i].moveI;
            int nextJ = currentJ + moveMonkey[i].moveJ;
            if(nextI >= 0 && nextI < M && nextJ >= 0 && nextJ < N){
                if(!visited[nextI][nextJ][currentH] && map[nextI][nextJ] != 1){
                    dq.push_back(make_pair(make_pair(nextI, nextJ), make_pair(currentH, currentD + 1)));
                    visited[nextI][nextJ][currentH] = true;
                }
            }
        }
    }
    cout << -1 << endl;
}

int main(){
    cin >> K >> N >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    BFS();
    return 0;
}

/*
1
2 2
0 1
1 0
Answer : -1

1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
Answer : 4

1
1 1
0
Answer : 0

1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
Answer : 6


*/


/*
4 4
####
#JF#
#..#
#..#
-> 3

5 5
##.##
#...#
#FJ.#
#...#
#####
-> 3

3 3
###
#J.
#.F
-> IMPOSSIBLE

5 5
....F
...J#
....#
....#
...#.
-> 4

3 3
F.F
.J.
F.F
-> IMPOSSIBLE

1 1 
J
-> 1
*/
