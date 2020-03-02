#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <deque>

using namespace std;

int main(){
    int I = 10 , J = 10;
    int currentI = 3, currentJ = 7;
    int nextI, nextJ;
    int map[20][20];
    for(int i = 0 ; i < 10 ; i++){
        nextI = I - (J - currentJ);
        nextJ = J + (I - currentI);
        currentI = nextI;
        currentJ = nextJ;
        memset(map, 0 , sizeof(map));
        map[currentI][currentJ] = 1;
        for(int i = 0 ; i < 20 ; i++){
            for(int j = 0 ; j < 20 ; j++){
                cout << map[i][j];
            }
            cout << "\n";
        }
        cout << "\n";
    }
    return 0;
}