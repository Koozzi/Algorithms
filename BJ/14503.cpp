#include <iostream>

using namespace std;

int M, N, currentI, currentJ, nextI, nextJ, rotCnt, dir;
int map[50][50];

void nextLocation(){
    if(dir == 0){
        nextI = currentI;
        nextJ = currentJ - 1;
    }else if(dir == 1){
        nextI = currentI - 1;
        nextJ = currentJ;
    }else if(dir == 2){
        nextI = currentI;
        nextJ = currentJ + 1;        
    }else{
        nextI = currentI + 1;
        nextJ = currentJ;
    }
}
void forward(){
    if(dir == 0){
        currentI = currentI - 1;
        currentJ = currentJ;
    }else if(dir == 1){
        currentI = currentI;
        currentJ = currentJ + 1;
    }else if(dir == 2){
        currentI = currentI + 1;
        currentJ = currentJ;        
    }else{
        currentI = currentI;
        currentJ = currentJ - 1;
    }
    rotCnt = 0;
}
void backward(){
    if(dir == 0){
        currentI = currentI + 1;
        currentJ = currentJ;
    }else if(dir == 1){
        currentI = currentI;
        currentJ = currentJ - 1;
    }else if(dir == 2){
        currentI = currentI - 1;
        currentJ = currentJ;        
    }else{
        currentI = currentI;
        currentJ = currentJ + 1;
    }   
    rotCnt = 0; 
}
void changeDir(){
    if(dir == 0){
        dir = 3;
    }else if(dir == 1){
        dir = 0;
    }else if(dir == 2){
        dir = 1;
    }else{
        dir = 2;
    }
    rotCnt++;
}
void letsClean(){
    rotCnt = 0;
    while(1){
        nextLocation();
        if(map[nextI][nextJ] == 0){
            changeDir();
            forward();
            map[currentI][currentJ] = 8;
        }
        else if((map[nextI][nextJ] == 8 || map[nextI][nextJ] == 1) && rotCnt < 4){
            changeDir();
        }
        else if(rotCnt == 4){
            backward();
            if(map[currentI][currentJ] == 1){
                break;
            }
        }
    }
}

int main(){
    cin >> M >> N >> currentI >> currentJ >> dir ;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    map[currentI][currentJ] = 8;
    letsClean();
    int ans = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] == 8){
                ans++;
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
