#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int primeNum[10001] = {0};

void eratos(){
    for(int i = 2 ; i * i < 10001 ; i++){
        for(int j = i * i ; j < 10001 ; j += i){
            primeNum[j] = 1;
        }
    }
}

int main(){
    int num_arr[4] = {0};
    int current = 4567;
    num_arr[0] = current / 1000;
    num_arr[1] = (current - 1000 * num_arr[0]) / 100;
    num_arr[2] = (current - 1000 * num_arr[0] - 100 * num_arr[1]) / 10;
    num_arr[3] = current - 1000 * num_arr[0] - 100 * num_arr[1] - 10 * num_arr[2];
    int next = 1000 * num_arr[0] + 100 * num_arr[1] + 10 * num_arr[2] + num_arr[3];
    cout << current << "\n";
    for(int i = 0 ; i < 4 ; i++){
        cout << num_arr[i] << "\n";
    }
    cout << next << "\n";
    return 0;
}