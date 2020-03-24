#include <iostream>

using namespace std;

int M;
int map[100][100];
long long int dp[100][100];

void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cout << dp[i][j] << " ";
        }cout << endl;
    }
}

int main(){
    cin >> M;
    dp[0][0] = 1;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
            if(dp[i][j] != 0 && map[i][j] != 0){
                int nextI = i + map[i][j];
                int nextJ = j + map[i][j];
                if(nextI < M && nextJ < M){
                    dp[i][nextJ] += dp[i][j];
                    dp[nextI][j] += dp[i][j]; 
                }
                else if(nextI < M && nextJ >= M){
                    dp[nextI][j] += dp[i][j];
                }
                else if(nextI >= M && nextJ < M){
                    dp[i][nextJ] += dp[i][j];
                }
            }
        }
    }
    cout << dp[M-1][M-1] << endl;
    return 0;
}

/*
4     
1 1 1 1
1 1 1 1
1 1 1 2
1 1 2 0
-> 0

4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
-> 3

4
3 0 0 3
0 0 0 0
0 0 0 0
3 0 0 0
-> 2

4
2 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
-> 0

4
2 1 0 4
2 3 3 3
0 2 3 4
2 3 1 0
-> 0

4
9 1 2 3
1 1 1 1
1 1 1 1
1 1 1 0
-> 0
*/