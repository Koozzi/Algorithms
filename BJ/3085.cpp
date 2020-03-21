#include <iostream>
#include <algorithm>

using namespace std;

int M, cnt, ans = 0;
char map[51][51];
void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cout << map[i][j] << " ";
        }cout << endl;
    }
}
void count(int I, int J){
    cnt = 0;
    for(int i = I - 1 ; i >= 0 ; i--){ // 위
        if(map[i][J] == map[I][J]){
            cnt++;
        }
        else{
            break;
        }
    }
    for(int i = I + 1 ; i < M ; i++){
        if(map[i][J] == map[I][J]){
            cnt++;
        }
        else{
            break;
        }
    }
    ans = max(ans, cnt + 1);
    cnt = 0;
    for(int j = J + 1 ; j < M ; j++){
        if(map[I][j] == map[I][J]){
            cnt++;
        }
        else{
            break;
        }
    }
    for(int j = J - 1 ; j >= 0 ; j--){
        if(map[I][j] == map[I][J]){
            cnt++;
        }
        else{
            break;
        }
    }
    ans = max(ans, cnt + 1);
}
void changeValue(int I, int J, int nI, int nJ){
    char tmp = map[I][J];
    map[I][J] = map[nI][nJ];
    map[nI][nJ] = tmp;
}
void changeRight(int I, int J){
    char tmp;
    int nextI = I;
    int nextJ = J + 1;
    if(nextJ < M){
        changeValue(I, J, nextI, nextJ);
        count(I,J);
        count(nextI, nextJ);
        changeValue(I, J, nextI, nextJ);
    }
    else{
        count(I,J);
    }
}
void changeLeft(int I, int J){
    char tmp;
    int nextI = I;
    int nextJ = J - 1;
    if(nextJ >= 0){
        changeValue(I, J, nextI, nextJ);
        count(I,J);
        count(nextI, nextJ);
        changeValue(I, J, nextI, nextJ);
    }
    else{
        count(I,J);
    }
}
void changeUp(int I, int J){
    char tmp;
    int nextI = I - 1;
    int nextJ = J;
    if(nextI >= 0){
        changeValue(I, J, nextI, nextJ);
        count(I,J);
        count(nextI, nextJ);
        changeValue(I, J, nextI, nextJ);
    }
    else{
        count(I,J);
    }
}
void changeDown(int I, int J){
    char tmp;
    int nextI = I + 1;
    int nextJ = J;
    if(nextI < M){
        changeValue(I, J, nextI, nextJ);
        count(I,J);
        count(nextI, nextJ);
        changeValue(I, J, nextI, nextJ);
    }
    else{
        count(I,J);
    }
}
int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            changeDown(i,j);
            changeLeft(i,j);
            changeRight(i,j);
            changeUp(i,j);
        }
    }
    cout << ans << endl;
    return 0;
}