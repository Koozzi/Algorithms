#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N, ans = 11;
int redI, redJ, blueI, blueJ, holeI, holeJ;
char map[11][11];
char cmap[11][11];

vector<int> v;
vector<int> tmp;

void show(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << cmap[i][j];
        }cout<<"\n";
    }
}

void copyMap(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cmap[i][j] = map[i][j];
        }
    }
}

void rotate(int dir){
    if(dir == 1){

    }
}

void solve(int cnt){
    if(cnt == 10){
        copyMap();
        
        return;
    }
    else{
        cnt++;
        for(int i = 1 ; i < 5 ; i++){
            if(v[cnt-2] != i){
                v.push_back(i);
                solve(cnt);
                v.pop_back();
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
    }
    for(int i = 1; i < 5 ; i++){
        v.push_back(i);
        solve(1);
        v.pop_back();
    }
}