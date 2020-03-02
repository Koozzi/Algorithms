#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int M, N, locI, locJ, Num;
int map[20][20];
int commend[1000];
int diceNum[6] = {0,0,0,0,0,0};

void rotate(int com);
void rotateEast();
void rotateWest();
void rotateNorth();
void rotateSouth();

int main(){
    cin >> M >> N >> locI >> locJ >> Num;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    for(int i = 0 ; i < Num ; i++){
        cin >> commend[i];
        rotate(commend[i]);
    }
    return 0;

}

void rotate(int com){
    if(com == 1){
        rotateEast();
    }
    else if(com == 2){
        rotateWest();
    }
    else if(com == 3){
        rotateNorth();
    }
    else{
        rotateSouth();
    }
}

void rotateEast(){
    int nextJ = locJ + 1;
    if(nextJ < N){
        locJ = nextJ;
        int copyArr[6];
        for(int i = 0 ; i < 6 ; i++){
            copyArr[i] = diceNum[i]; 
        }
        diceNum[0] = copyArr[5];
        diceNum[1] = copyArr[3];
        diceNum[3] = copyArr[0];
        diceNum[5] = copyArr[1];
        if(map[locI][locJ] == 0){
            map[locI][locJ] = diceNum[1];
        }
        else{
            diceNum[1] = map[locI][locJ];
            map[locI][locJ] = 0;
        }
        cout << diceNum[0] << "\n";
    }
}
void rotateWest(){
    int nextJ = locJ - 1;
    if(nextJ >= 0){
        locJ = nextJ;
        int copyArr[6];
        for(int i = 0 ; i < 6 ; i++){
            copyArr[i] = diceNum[i]; 
        }
        diceNum[0] = copyArr[3];
        diceNum[1] = copyArr[5];
        diceNum[3] = copyArr[1];
        diceNum[5] = copyArr[0];
        if(map[locI][locJ] == 0){
            map[locI][locJ] = diceNum[1];
        }
        else{
            diceNum[1] = map[locI][locJ];
            map[locI][locJ] = 0;
        }
        cout << diceNum[0] << "\n";
    }
}
void rotateNorth(){
    int nextI = locI - 1;
    if(nextI >= 0){
        locI = nextI;
        int copyArr[6];
        for(int i = 0 ; i < 6 ; i++){
            copyArr[i] = diceNum[i]; 
        }
        diceNum[0] = copyArr[4];
        diceNum[1] = copyArr[2];
        diceNum[2] = copyArr[0];
        diceNum[4] = copyArr[1];
        if(map[locI][locJ] == 0){
            map[locI][locJ] = diceNum[1];
        }
        else{
            diceNum[1] = map[locI][locJ];
            map[locI][locJ] = 0;
        }
        cout << diceNum[0] << "\n";
    }
}
void rotateSouth(){
    int nextI = locI + 1;
    if(nextI < M){
        locI = nextI;
        int copyArr[6];
        for(int i = 0 ; i < 6 ; i++){
            copyArr[i] = diceNum[i]; 
        }
        diceNum[0] = copyArr[2];
        diceNum[1] = copyArr[4];
        diceNum[2] = copyArr[1];
        diceNum[4] = copyArr[0];
        if(map[locI][locJ] == 0){
            map[locI][locJ] = diceNum[1];
        }
        else{
            diceNum[1] = map[locI][locJ];
            map[locI][locJ] = 0;
        }
        cout << diceNum[0] << "\n";
    }
}