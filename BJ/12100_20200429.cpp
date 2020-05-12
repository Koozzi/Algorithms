#include <iostream>
using namespace std;

int M;
int map[20][20];

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
        }
    }
}