#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <memory.h>

using namespace std;

deque<int> gear[5];

int M;
char inputData[9];
int rotationDir[5];

void rotateRight(int idx){
    int a = gear[idx].back();
    gear[idx].push_front(a);
    gear[idx].pop_back();
}
void rotateLeft(int idx){
    int a = gear[idx].front();
    gear[idx].push_back(a);
    gear[idx].pop_front();
}
void rotate(int gearNum, int direction){
    memset(rotationDir, 0, sizeof(rotationDir));
    rotationDir[gearNum] = direction;
    for(int i = gearNum ; i > 1 ; i--){
        if(gear[i][6] != gear[i-1][2]){
            if(rotationDir[i] == 1){
                rotationDir[i-1] = -1;
            }
            else{
                rotationDir[i-1] = 1;
            }
        }
        else{
            break;
        }
    }
    for(int i = gearNum ; i < 4 ; i++){
        if(gear[i][2] != gear[i+1][6]){
            if(rotationDir[i] == 1){
                rotationDir[i+1] = -1;
            }
            else{
                rotationDir[i+1] = 1;
            }
        }
        else{
            break;
        }
    }
    for(int i = 1 ; i <= 4 ; i++){
        if(rotationDir[i] == 1){
            rotateRight(i);
        }
        else if(rotationDir[i] == -1){
            rotateLeft(i);
        }
    }
}

int main(){
    for(int t = 1 ; t <= 4 ; t++){
        cin >> inputData;
        for(int i = 0 ; i < 8 ; i++){
            gear[t].push_back(int(inputData[i]) - 48);
        }
    }
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a , b;
        cin >> a >> b;
        rotate(a,b);
    }
    int ans = 0;
    int mult = 1;
    for(int i = 1 ; i <= 4 ; i++){
        if(gear[i][0] == 1){
            ans += mult;
        }
        mult = mult * 2;
    }
    cout << ans << "\n";
    return 0;
}
