#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N, idx = 0;
char M[10];

int charInt(){
    int intNum = 0;
    int newIdx = idx;
    int mult = 1;
    while(newIdx > 0){
        intNum += ((M[newIdx-1] - 48) * mult);
        mult = mult * 10;
        newIdx--;
    }
    return intNum;
}

int main(){
    cin >> M >> N;
    while(1){
        if(M[idx] == '\0'){
            break;
        }
        idx++;
    }
    for(int i = 0 ; i < 10 ; i++){
        for(int j = 0 ; j < 10 ; j++){
            M[idx-2] = i + 48;
            M[idx-1] = j + 48;
            if(charInt() % N == 0){
                cout << i << j << "\n";
                return 0;
            }
        }
    }
}