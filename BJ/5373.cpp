#include <iostream>
#include <memory.h>

using namespace std;

char order[1001][3];

char StartCube[6][3][3] = {
    {{'w', 'w', 'w'}, {'w', 'w', 'w'}, {'w', 'w', 'w'}},
    {{'y', 'y', 'y'}, {'y', 'y', 'y'}, {'y', 'y', 'y'}},
    {{'r', 'r', 'r'}, {'r', 'r', 'r'}, {'r', 'r', 'r'}},
    {{'g', 'g', 'g'}, {'g', 'g', 'g'}, {'g', 'g', 'g'}},
    {{'o', 'o', 'o'}, {'o', 'o', 'o'}, {'o', 'o', 'o'}},
    {{'b', 'b', 'b'}, {'b', 'b', 'b'} ,{'b', 'b', 'b'}},
};
char CopiedCube[6][3][3];
char OriginalCube[6][3][3];
void showC(){
    cout << endl;
    for(int t = 0 ; t < 6 ; t++){
        for(int i = 0 ; i < 3 ; i++){
            for(int j = 0 ; j < 3 ; j++){
                cout << CopiedCube[t][i][j] << " ";
            }cout << endl;
        }cout << endl;
    }
}
void showO(){
    cout << endl;
    for(int t = 0 ; t < 6 ; t++){
        for(int i = 0 ; i < 3 ; i++){
            for(int j = 0 ; j < 3 ; j++){
                cout << OriginalCube[t][i][j] << " ";
            }cout << endl;
        }cout << endl;
    }
}
void start(){
    for(int t = 0 ; t < 6 ; t++){
        for(int i = 0 ; i < 3 ; i++){
            for(int j = 0 ; j < 3 ; j++){
                OriginalCube[t][i][j] = StartCube[t][i][j];
            }
        }
    }    
}
void copyCube(){
    for(int t = 0 ; t < 6 ; t++){
        for(int i = 0 ; i < 3 ; i++){
            for(int j = 0 ; j < 3 ; j++){
                CopiedCube[t][i][j] = OriginalCube[t][i][j];
            }
        }
    }
}
void rotatePlane(int plane, char dir){
    // copyCube();
        if(dir == '+'){
            for(int i = 0 ; i < 3 ; i++){
                OriginalCube[plane][i][0] = CopiedCube[plane][2][i];
                OriginalCube[plane][2][i] = CopiedCube[plane][2-i][2];
                OriginalCube[plane][i][2] = CopiedCube[plane][0][i];
                OriginalCube[plane][0][i] = CopiedCube[plane][2-i][0];
            }
        }
        else{
            for(int i = 0 ; i < 3 ; i++){
                OriginalCube[plane][i][0] = CopiedCube[plane][0][2-i];
                OriginalCube[plane][0][i] = CopiedCube[plane][i][2];
                OriginalCube[plane][i][2] = CopiedCube[plane][2][2-i];
                OriginalCube[plane][2][i] = CopiedCube[plane][i][0];
            }
        }
}
void rotateU(char dir){
    // copyCube();
    if(dir == '+'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[5][0][i] = CopiedCube[4][0][i]; // 뒤 -> 오
            OriginalCube[2][0][i] = CopiedCube[5][0][i]; // 오 -> 앞
            OriginalCube[3][0][i] = CopiedCube[2][0][i]; // 앞 -> 왼
            OriginalCube[4][0][i] = CopiedCube[3][0][i]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[4][0][i] = CopiedCube[5][0][i]; // 뒤 -> 오
            OriginalCube[5][0][i] = CopiedCube[2][0][i]; // 오 -> 앞
            OriginalCube[2][0][i] = CopiedCube[3][0][i]; // 앞 -> 왼
            OriginalCube[3][0][i] = CopiedCube[4][0][i]; // 왼 -> 뒤
        }        
    }
    rotatePlane(0, dir);
}
void rotateD(char dir){
    // copyCube();
    if(dir == '-'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[5][2][i] = CopiedCube[4][2][i]; // 뒤 -> 오
            OriginalCube[2][2][i] = CopiedCube[5][2][i]; // 오 -> 앞
            OriginalCube[3][2][i] = CopiedCube[2][2][i]; // 앞 -> 왼
            OriginalCube[4][2][i] = CopiedCube[3][2][i]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[4][2][i] = CopiedCube[5][2][i]; // 뒤 -> 오
            OriginalCube[5][2][i] = CopiedCube[2][2][i]; // 오 -> 앞
            OriginalCube[2][2][i] = CopiedCube[3][2][i]; // 앞 -> 왼
            OriginalCube[3][2][i] = CopiedCube[4][2][i]; // 왼 -> 뒤
        }        
    }
    rotatePlane(1, dir);
}
void rotateR(char dir){
    // copyCube();
    if(dir == '+'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[0][i][2] = CopiedCube[2][i][2]; // 뒤 -> 오
            OriginalCube[4][2-i][0] = CopiedCube[0][i][2]; // 오 -> 앞
            OriginalCube[1][i][2] = CopiedCube[4][2-i][0]; // 앞 -> 왼
            OriginalCube[2][i][2] = CopiedCube[1][i][2]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[2][i][2] = CopiedCube[0][i][2]; // 뒤 -> 오
            OriginalCube[0][i][2] = CopiedCube[4][2-i][0]; // 오 -> 앞
            OriginalCube[4][2-i][0] = CopiedCube[1][i][2]; // 앞 -> 왼
            OriginalCube[1][i][2] = CopiedCube[2][i][2]; // 왼 -> 뒤
        }        
    }
    rotatePlane(5, dir);
}
void rotateF(char dir){
    // copyCube();
    if(dir == '+'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[0][2][i] = CopiedCube[3][2-i][2]; // 뒤 -> 오
            OriginalCube[3][2-i][2] = CopiedCube[1][0][i]; // 오 -> 앞
            OriginalCube[1][0][i] = CopiedCube[5][i][0]; // 앞 -> 왼
            OriginalCube[5][i][0] = CopiedCube[0][2][i]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[3][2-i][2] = CopiedCube[0][2][i]; // 뒤 -> 오
            OriginalCube[1][0][i] = CopiedCube[3][2-i][2]; // 오 -> 앞
            OriginalCube[5][i][0] = CopiedCube[1][0][i]; // 앞 -> 왼
            OriginalCube[0][2][i] = CopiedCube[5][i][0]; // 왼 -> 뒤
        }        
    }
    rotatePlane(2, dir);
}
void rotateL(char dir){
    // copyCube();
    if(dir == '+'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[2][i][0] = CopiedCube[0][i][0]; // 뒤 -> 오
            OriginalCube[0][i][0] = CopiedCube[4][2-i][2]; // 오 -> 앞
            OriginalCube[4][2-i][2] = CopiedCube[1][i][0]; // 앞 -> 왼
            OriginalCube[1][i][0] = CopiedCube[2][i][0]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[0][i][0] = CopiedCube[2][i][0]; // 뒤 -> 오
            OriginalCube[4][2-i][2] = CopiedCube[0][i][0]; // 오 -> 앞
            OriginalCube[1][i][0] = CopiedCube[4][2-i][2]; // 앞 -> 왼
            OriginalCube[2][i][0] = CopiedCube[1][i][0]; // 왼 -> 뒤
        }        
    }
    rotatePlane(3, dir);
}
void rotateB(char dir){
    // copyCube();
    if(dir == '-'){
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[0][0][i] = CopiedCube[3][2-i][0]; // 뒤 -> 오
            OriginalCube[3][2-i][0] = CopiedCube[1][2][i]; // 오 -> 앞
            OriginalCube[1][2][i] = CopiedCube[5][i][2]; // 앞 -> 왼
            OriginalCube[5][i][2] = CopiedCube[0][0][i]; // 왼 -> 뒤
        }
    }
    else{
        for(int i = 0 ; i < 3 ; i++){
            OriginalCube[0][0][i] = CopiedCube[5][i][2]; // 뒤 -> 오
            OriginalCube[5][i][2] = CopiedCube[1][2][i]; // 오 -> 앞
            OriginalCube[1][2][i] = CopiedCube[3][2-i][0]; // 앞 -> 왼
            OriginalCube[3][2-i][0] = CopiedCube[0][0][i]; // 왼 -> 뒤
        }       
    }
    rotatePlane(4, dir);
}
void showAns(){
    for(int i = 0 ; i < 3 ; i++){
        for(int j = 0 ; j < 3 ; j++){
            cout << OriginalCube[0][i][j];
        }cout << endl;
    }
}

int main(){
    int T;
    cin >> T;
    while(T--){
        memset(order, '\0', sizeof(order));
        start();
        int Num;
        cin >> Num;
        for(int i = 0 ; i < Num ; i++){
            cin >> order[i];
            copyCube();
            if(order[i][0] == 'U'){
                rotateU(order[i][1]);
            }
            else if(order[i][0] == 'D'){
                rotateD(order[i][1]);
            }
            else if(order[i][0] == 'R'){
                rotateR(order[i][1]);
            }
            else if(order[i][0] == 'L'){
                rotateL(order[i][1]);
            }
            else if(order[i][0] == 'F'){
                rotateF(order[i][1]);
            }
            else{
                rotateB(order[i][1]);
            }
        }
        showAns();
    }
    return 0;
}