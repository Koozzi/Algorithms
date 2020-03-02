#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int M, N, ans = 65;
int map[8][8];
int cmap[8][8];

vector<pair<pair<int, int>, pair<int, int>>> v;
vector<pair<int, int>> cctv;

void show(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << cmap[i][j] << " ";
        }
        cout << "\n";
    }
}

void copyMap(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cmap[i][j] = map[i][j];
        }
    }
}

void up(int startI, int startJ){
    for(int i = startI - 1 ; i >= 0 ; i--){
        if(cmap[i][startJ] == 6){
            return;
        }
        if(cmap[i][startJ] == 0){
            cmap[i][startJ] = 9;
        }
    }
}

void down(int startI, int startJ){
    for(int i = startI + 1 ; i < M ; i++){
        if(cmap[i][startJ] == 6){
            return;
        }
        if(cmap[i][startJ] == 0){
            cmap[i][startJ] = 9;
        }
    }
}

void right(int startI, int startJ){
    for(int i = startJ + 1 ; i < N ; i++){
        if(cmap[startI][i] == 6){
            return;
        }
        if(cmap[startI][i] == 0){
            cmap[startI][i] = 9;
        }
    }
}

void left(int startI, int startJ){
    for(int i = startJ - 1 ; i >= 0 ; i--){
        if(cmap[startI][i] == 6){
            return;
        }
        if(cmap[startI][i] == 0){
            cmap[startI][i] = 9;
        }
    }
}

void One(int num, int dir){
    if(dir == 0){
        right(v[num].first.first, v[num].first.second);
    }
    else if(dir == 1){
        down(v[num].first.first, v[num].first.second);
    }
    else if(dir == 2){
        left(v[num].first.first, v[num].first.second);
    }
    else{
        up(v[num].first.first, v[num].first.second);
    }
}

void Two(int num, int dir){
    if(dir == 0){
        right(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else if(dir == 1){
        down(v[num].first.first, v[num].first.second);
        up(v[num].first.first, v[num].first.second);
    }
    else if(dir == 2){
        right(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else{
        up(v[num].first.first, v[num].first.second);
        down(v[num].first.first, v[num].first.second);
    }
}
void Three(int num, int dir){
    if(dir == 0){
        right(v[num].first.first, v[num].first.second);
        down(v[num].first.first, v[num].first.second);
    }
    else if(dir == 1){
        down(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else if(dir == 2){
        up(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else{
        up(v[num].first.first, v[num].first.second);
        right(v[num].first.first, v[num].first.second);
    }
}
void Four(int num, int dir){
    if(dir == 0){
        up(v[num].first.first, v[num].first.second);
        right(v[num].first.first, v[num].first.second);
        down(v[num].first.first, v[num].first.second);
    }
    else if(dir == 1){
        right(v[num].first.first, v[num].first.second);
        down(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else if(dir == 2){
        down(v[num].first.first, v[num].first.second);
        up(v[num].first.first, v[num].first.second);
        left(v[num].first.first, v[num].first.second);
    }
    else{
        left(v[num].first.first, v[num].first.second);
        up(v[num].first.first, v[num].first.second);
        right(v[num].first.first, v[num].first.second);
    }
}
void Five(int num, int dir){
        left(v[num].first.first, v[num].first.second);
        up(v[num].first.first, v[num].first.second);
        right(v[num].first.first, v[num].first.second);
        down(v[num].first.first, v[num].first.second);
}

void camera(int num){
    if(cctv[num].first == 1){
        One(num, cctv[num].second);
    }
    else if(cctv[num].first == 2){
        Two(num, cctv[num].second);
    }
    else if(cctv[num].first == 3){
        Three(num, cctv[num].second);
    }
    else if(cctv[num].first == 4){
        Four(num, cctv[num].second);
    }
    else{
        Five(num, cctv[num].second);
    }
}

void watch(int cnt){
    if(cctv.size() == v.size()){
        copyMap();
        for(int i = 0 ; i < cctv.size() ; i++){
            camera(i);
        }
        int zeroCount = 0;
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                if(cmap[i][j] == 0){
                    zeroCount++;
                }
            }
        }
        // if(zeroCount == 2){
        //     show();
        //     cout << "\n";
        // }
        // show();
        // cout << zeroCount << "\n";
        // cout << "\n";
        ans = min(ans, zeroCount);
        return;
    }
    else{
        cnt++;
        for(int i = 0 ; i < 4 ; i++){
            cctv.push_back(make_pair(map[v[cnt].first.first][v[cnt].first.second], i));
            watch(cnt);
            cctv.pop_back();
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
            if(map[i][j] != 0 && map[i][j] != 6){
                v.push_back(make_pair(make_pair(i,j), make_pair(map[i][j], 0)));
            }
        }
    }
    if(v.size() == 0){
        int otherAns = 0;
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < N ; j++){
                if(map[i][j] == 0){
                    otherAns++;
                }
            }
        }
        cout << otherAns << "\n";
    }
    else{
        watch(-1);
        cout << ans << "\n";
    }

    return 0;
}