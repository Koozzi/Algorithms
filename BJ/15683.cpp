#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// vector<pair<pair<int, int>, pair<int, int>>> cctv;
int M, N;
int map[8][8];

typedef struct{
    int locI, locJ;
    int cctvNum;
    int N, E, S, W;
}CCTV;
CCTV cctvInfo[8];

void make(int startI, int startJ, int dir){
    if(dir == 1){
        for(int i = startI - 1 ; i >= 0 ; i--){ // N
            if(map[i][startJ] == 6){
                break;
            }
            if(map[i][startJ] == 0){
                map[i][startJ] = -1;
            }
        }
    }
    else if(dir == 2){
        for(int i = startJ + 1 ; i < N ; i++){ // E
            if(map[startI][i] == 6){
                break;
            }
            if(map[startI][i] == 0){
                map[startI][i] = -1;
            }
        }
    }
    else if(dir == 3){
        for(int i = startI + 1 ; i < M ; i++){ // S
            if(map[i][startJ] == 6){
                break;
            }
            if(map[i][startJ] == 0){
                map[i][startJ] = -1;
            }
        }
    }
    else{
        for(int i = startJ -1 ; i >= N ; i--){ // W
            if(map[startI][i] == 6){
                break;
            }
            if(map[startI][i] == 0){
                map[startI][i] = -1;
            }
        }
    }
}

int main(){
    int cctvCount = 0;
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j] != 0 && map[i][j] != 6){
                int A = 0;
                cctvInfo[cctvCount].locI = i;
                cctvInfo[cctvCount].locJ = j;
                cctvInfo[cctvCount].cctvNum = map[i][j];
                for(int cctvI = i - 1; cctvI >= 0 ; cctvI--){
                    if(map[cctvI][j] == 6){
                        break;
                    }
                    A++;
                }
                cctvInfo[cctvCount].N = A;
                A = 0;
                for(int cctvJ = j + 1; cctvJ < N ; cctvJ++){
                    if(map[i][cctvJ] == 6){
                        break;
                    }
                    A++;
                }
                cctvInfo[cctvCount].E = A;
                A = 0;
                for(int cctvI = i + 1; cctvI < M ; cctvI++){
                    if(map[cctvI][j] == 6){
                        break;
                    }
                    A++;
                }
                cctvInfo[cctvCount].S = A;
                A = 0;
                for(int cctvJ = j - 1; cctvJ >= 0 ; cctvJ--){
                    if(map[i][cctvJ] == 6){
                        break;
                    }
                    A++;
                }
                cctvInfo[cctvCount].W = A;
                cctvCount++;
            }
        }
    }
    for(int i = 0 ; i < cctvCount ; i++){
        if(cctvInfo[i].cctvNum == 1){
            int direction = 0;
            int maxCount = 0;
            if(cctvInfo[i].N >= maxCount){
                maxCount = cctvInfo[i].N;
                direction = 1;
            }
            else if(cctvInfo[i].E >= maxCount){
                maxCount = cctvInfo[i].E;
                direction = 2;
            }            
            else if(cctvInfo[i].S >= maxCount){
                maxCount = cctvInfo[i].S;
                direction = 3;
            }            
            else if(cctvInfo[i].W >= maxCount){
                maxCount = cctvInfo[i].W;
                direction = 4;
            }
            make(cctvInfo[i].locI, cctvInfo[i].locJ, direction);
        }
        else if(cctvInfo[i].cctvNum == 2){

        }
        else if(cctvInfo[i].cctvNum == 3){

        }
        else if(cctvInfo[i].cctvNum == 4){

        }
        else{

        }
    }
    for(int i = 0 ; i < cctvCount ; i++){
        cout << "location : " << cctvInfo[i].locI << "," << cctvInfo[i].locJ << "\n";
        cout << "N : " << cctvInfo[i].N << "\n";
        cout << "E : " << cctvInfo[i].E << "\n";
        cout << "S : " << cctvInfo[i].S << "\n";
        cout << "W : " << cctvInfo[i].W << "\n";
    }
}



