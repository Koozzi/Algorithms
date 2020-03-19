#include <iostream>
#include <cmath>

using namespace std;

int M, cnt = 0, ans = 0;

int map[15][15];

bool isPossible(int I, int J){
    // for(int i = 0 ; i < I ; i++){
    //     for(int j = 0 ; j < M ; j++){
    //         if(abs(i - I) == abs(j - J)){
    //             if(map[i][j] == 1){
    //                 return false;
    //             }
    //         }
    //         if(j == J){
    //             if(map[i][j] == 1){
    //                 return false;
    //             }
    //         }
    //     }
    // }
    // return true;
    int nextI, nextJ;

    //위 
    nextI = I - 1;
    nextJ = J;
    while(nextI >= 0){
        if(map[nextI][nextJ] == 1){
            return false;
        }
        nextI--;
    }

    //오
    nextI = I;
    nextJ = J + 1;
    while(nextJ < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }
        nextJ++;
    }

    //아래
    nextI = I + 1;
    nextJ = J;
    while(nextI < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }
        nextI++;
    }
    // Left
    nextI = I;
    nextJ = J - 1;
    while(nextJ >= 0){
        if(map[nextI][nextJ] == 1){
            return false;
        }
        nextJ--;
    }

    // Left Up
    nextI = I - 1;
    nextJ = J - 1;
    while(nextI >= 0 && nextJ >= 0 && nextI < M && nextJ < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }   
        nextI--;
        nextJ--;      
    }

    // Right Up
    nextI = I - 1;
    nextJ = J + 1;
    while(nextI >= 0 && nextJ >= 0 && nextI < M && nextJ < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }   
        nextI--;
        nextJ++;      
    }

    nextI = I + 1;
    nextJ = J + 1;
    while(nextI >= 0 && nextJ >= 0 && nextI < M && nextJ < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }   
        nextI++;
        nextJ++;      
    }

    nextI = I + 1;
    nextJ = J - 1;
    while(nextI >= 0 && nextJ >= 0 && nextI < M && nextJ < M){
        if(map[nextI][nextJ] == 1){
            return false;
        }   
        nextI++;
        nextJ--;      
    }
    return true;
}

void DFS(int line){
    if(cnt == M){
        ans++;
    }
    else{
        for(int i = 0 ; i < M ; i++){
            if(isPossible(line, i)){
                cnt++;
                map[line][i] = 1;
                DFS(line + 1);
                map[line][i] = 0;
                cnt--;
            }
        }
    }
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cnt++;
        map[0][i] = 1;
        DFS(1);
        map[0][i] = 0;
        cnt--;
    }
    cout << ans << endl;
    return 0;
}