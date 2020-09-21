#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int N;
int map[10];

int main(){
    int T; cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> N;
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < N ; j++){
                cin >> map[i][j];
            }
        }
    }
}