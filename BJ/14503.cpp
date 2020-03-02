#include <iostream>

using namespace std;

int map[50][50];

int M, N, locI, locJ, dir, nextI, nextJ;

void foward(int I, int J, int Dir);
void backward(int I, int J, int Dir);
void changeDir(int Dir);
void letsClean(int I, int J, int Dir);

int main(){
    cin >> M >> N >> locI >> locJ >> dir;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
}

void changeDir(int Dir){
    if(Dir == 1){
        dir = 4;
    }
    else if(Dir == 2){
        dir = 1;
    }
    else if(Dir == 3){
        dir = 2;
    }
    else if(Dir == 4){
        dir = 3;
    }
}

void foward(int I, int J, int Dir){
    if(Dir == 1){
        locI = I - 1; 
        locJ = J;
    }
    else if(Dir == 2){
        locI = I;
        locJ = J + 1;
    }
    else if(Dir == 3){
        locI = I + 1;
        locJ = J;
    }
    else if(Dir == 4){
        locI = I;
        locJ = J - 1;
    }
}
void backward(int I, int J, int Dir){
    if(Dir == 1){
        locI = I + 1; 
        locJ = J;
    }
    else if(Dir == 2){
        locI = I;
        locJ = J - 1;
    }
    else if(Dir == 3){
        locI = I - 1;
        locJ = J;
    }
    else if(Dir == 4){
        locI = I;
        locJ = J + 1;
    }
}

void letsClean(int I, int J, int Dir){
    if(Dir == 1){
        I = I;
        J = J - 1;
        if(I >= 0 && I < M && J >= 0 && J < N){
            if(map[nextI][nextJ] == 0){
                changeDir(Dir);
            }
        }
    }
    else if(Dir == 2){

    }
    else if(Dir == 3){

    }
    else{

    }
}