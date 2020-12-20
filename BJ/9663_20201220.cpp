#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int N, answer;
bool board[15][15];

bool undertake(int I, int J){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(i == I && j == J) continue;
            if((i == I || j == J) && board[i][j]) return false;
            if((abs(i - I) == abs(j - J)) && board[i][j]) return false;
        }
    }
    return true;
}

void N_Queen(int start, int cnt){
    if(cnt == N){
        answer += 1;
        return;
    }

    for(int j = 0 ; j < N ; j++){
        if(!undertake(start, j)) continue;
        board[start][j] = true;
        N_Queen(start + 1, cnt + 1);
        board[start][j] = false;
    }
}

int main(){
    cin >> N;

    for(int i = 0 ; i < N ; i++){
        board[0][i] = true;
        N_Queen(1, 1);
        board[0][i] = false;
    }

    cout << answer << "\n";
    return 0;
}





