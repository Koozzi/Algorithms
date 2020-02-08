#include <iostream>

using namespace std;

int main(){
    char inputData[16][16];
    for(int i = 0 ; i < 16 ; i++){
        cin >> inputData[i];
    }
    cout << "-----------------------" << "\n";
    for(int i = 0 ; i < 16 ; i++){
        for(int j = 0 ; j < 16 ; j++){
            cout << inputData[i][j];
        }
        cout << "\n";
    }
    return 0;
}